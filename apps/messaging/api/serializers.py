from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers

from apps.messaging.models import MessageModel


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField()
    receiver = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    class Meta:
        model = MessageModel 
        fields = ["id", "created", "updated", "sender", "receiver", "message_content", "state", "deleted_date"]
        # Excluimos 'state' del formulario de creación
        read_only_fields = ['state']
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.state:
            del data["deleted_date"]   # Verifica si el mensaje está eliminado
        return data
    
    def create(self, validated_data):
        user = self.context['request'].user  # Obtiene el usuario autenticado desde el contexto
        validated_data['sender'] = user  # Establece el remitente como el usuario autenticado
                 
        message_content = MessageModel.objects.create(**validated_data)
        return message_content
    
    
    
class CustomJWTSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  

    class Meta:
        model = User
        fields = fields = [
            'id',
            'username',            
            'email', 
            'password'                 
        ]
        
    def create(self, validated_data):
        # Extrae la contraseña del campo y aplica el hashing
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  # Aplica el hashing a la contraseña
        user.save()
        return user
    
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'), username=username, password=password)

            if not user:
                raise serializers.ValidationError("Nombre de usuario o contraseña incorrectos.")
        else:
            raise serializers.ValidationError("Debe proporcionar un nombre de usuario y contraseña.")

        data['user'] = user
        return data



#TODO: reciever ahora se puede elegir, pero en la app deberá ser el el propietario que haya publicado su casa para alquilar
