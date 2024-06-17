from django.db.models import Q
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.abstracts.viewsets import AbstractViewSet
from apps.messaging.api.serializers import MessageSerializer
from apps.messaging.models import MessageModel
from utils.filters import MessageFilterSet
from utils.pagination import ExtendedPagination


#ViewSet para los mensajes
class MessageViewSet(AbstractViewSet):        
    serializer_class = MessageSerializer  
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = MessageFilterSet
    search_fields = ("sender", "receiver", "property")
    ordering_fields = ("sender", "receiver", "property")
    pagination_class = ExtendedPagination
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]  
    queryset = MessageModel.objects.all()

            
    def get_queryset(self):
        user = self.request.user
        # Filtrar los mensajes donde el usuario actual es el remitente o el receptor
        return MessageModel.objects.filter(Q(sender=user) | Q(receiver=user)) 
   
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Establecer el sender como el usuario autenticado
        sender = request.user
        receiver = serializer.validated_data.get('receiver', None)
        
        # Si no se proporciona un receiver, asignar el owner de la propiedad como receiver
        if not receiver:
            property_instance = serializer.validated_data['property']
            receiver = property_instance.owner
        
        # Crear el mensaje con el sender autenticado y el receiver determinado
        serializer.save(sender=sender, receiver=receiver)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        # Verificar si el usuario es el remitente del mensaje
        if instance.sender != request.user:
            return Response({'detail': 'No tienes permiso para editar este mensaje.'}, status=status.HTTP_403_FORBIDDEN)

        # Verificar si el mensaje fue enviado hace más de una semana
        one_week_ago = timezone.now() - timezone.timedelta(days=7)
        if instance.created < one_week_ago:
            return Response({'detail': 'No puedes editar un mensaje enviado hace más de una semana.'}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
    
    
    @action(detail=True, methods=['delete'])
    def delete(self, request, pk=None):
        message = self.get_object()
        message.is_active = False
        message.deleted_date = timezone.now()
        message.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
 