from rest_framework import serializers

from apps.abstracts.serializers import AbstractSerializer
from apps.messaging.models import MessageModel
from apps.properties.models import Property
from apps.users.models import User

#TODO: probar hacer propiedades en bd y poder enviar los mensajes de acuerdo a las propiedades asociadas

class MessageSerializer(AbstractSerializer, serializers.ModelSerializer):
    sender = serializers.StringRelatedField()
    receiver = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  
    receiver_username = serializers.ReadOnlyField(source="receiver.username") 
    property = serializers.PrimaryKeyRelatedField(queryset=Property.objects.all())  
    property_title = serializers.ReadOnlyField(source="property.title") 

    
    class Meta:
        model = MessageModel 
        fields = ["id", "created", "updated", "sender", "receiver", "receiver_username", "property", "property_title", "message_content", "deleted_date"]
        
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.is_active:
            del data["deleted_date"]   # Verifica si el mensaje está eliminado
        return data
    
    
    def create(self, validated_data):
        # Obtiene el usuario autenticado desde el contexto
        user = self.context['request'].user  
        
        # Establece el remitente como el usuario autenticado
        validated_data['sender'] = user
        
        # Llama al método create() del modelo MessageModel para crear el objeto
        message_content = MessageModel.objects.create(
        sender=validated_data['sender'],
        receiver=validated_data['receiver'],
        property=validated_data['property'],
        message_content=validated_data['message_content']
    )

        return message_content
    
"""   
    
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

"""

#TODO: reciever ahora se puede elegir, pero en la app deberá ser el el propietario que haya publicado su casa para alquilar
