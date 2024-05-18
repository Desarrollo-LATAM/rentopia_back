from rest_framework import serializers

from apps.abstracts.serializers import AbstractSerializer
from apps.messaging.models import MessageModel


class MessageSerializer(AbstractSerializer, serializers.ModelSerializer):
    sender = serializers.StringRelatedField()
    receiver_username = serializers.ReadOnlyField(source="receiver.username") 
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
        
        # Si no se proporciona un receiver, asignar el propietario de la propiedad como receiver
        if 'receiver' not in validated_data:
            validated_data['receiver'] = validated_data['property'].owner

        
        #validated_data['receiver'] = validated_data['property'].owner
        return super().create(validated_data)
    
        
  