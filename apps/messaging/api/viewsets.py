from rest_framework import viewsets
from apps.messaging.api.serializers import MessageSerializer
from apps.messaging.models import MessageModel


class MessageViewSet(viewsets.GenericViewSet):        
    serializer_class = MessageSerializer   
    queryset = MessageModel.objects.all()

            
    def get_queryset(self):
        print(self.request.user)  

        # Filtrar las tareas por el usuario autenticado
        return MessageModel.objects.filter(sender=self.request.user)
   
   
    # authentication_classes = [BasicAuthentication, JWTAuthentication]
    # permission_classes = [IsAuthenticated] 
    