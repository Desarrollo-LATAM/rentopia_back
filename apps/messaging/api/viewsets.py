from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils import timezone
from rest_framework import status, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken, Token

from apps.abstracts.viewsets import AbstractViewSet
from apps.messaging.api.serializers import MessageSerializer, UserSerializer
from apps.messaging.models import MessageModel


#ViewSet para el usuario
class UserViewSet(viewsets.ModelViewSet):    
    serializer_class = UserSerializer  
    queryset = User.objects.all()

    @action(detail=False, methods=['post'])
    def registro(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            id = serializer.validated_data['id']
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']            
            email = serializer.validated_data['email']

            # Crea un nuevo usuario
            user = User.objects.create_user(
                id=id,
                username=username,
                password=password,
                email=email
            )

            return Response({'message': 'Usuario registrado con éxito'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#ViewSet para el inicio de sesión
class LoginViewSet(viewsets.ViewSet):    
    @action(detail=False, methods=['post'])
    def iniciar_sesion(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            
            # Genera el token JWT
            access_token = str(Token.for_user(user).access)
            refresh_token = str(RefreshToken.for_user(user))
            
            print(f"Token JWT recibido: {access_token}")


            # Devuelve el token JWT en la respuesta
            return Response({'access_token': access_token, 'refresh_token': refresh_token,'message': 'Inicio de sesión exitoso'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Nombre de usuario o contraseña incorrectos'}, status=status.HTTP_401_UNAUTHORIZED)
        
        
#ViewSet para los mensajes
class MessageViewSet(AbstractViewSet):        
    serializer_class = MessageSerializer  
    authentication_classes = [BasicAuthentication, JWTAuthentication]
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
        serializer.validated_data['sender'] = request.user

       # Agregar el receptor al validated_data si está presente en la solicitud
        receiver_id = request.data.get('receiver')
        if receiver_id:
            receiver = User.objects.get(pk=receiver_id)
            serializer.validated_data['receiver'] = receiver
    
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    
    @action(detail=True, methods=['delete'])
    def delete(self, request, pk=None):
        message = self.get_object()
        message.is_active = False
        message.deleted_date = timezone.now()
        message.save()
        return Response(status=status.HTTP_204_NO_CONTENT)