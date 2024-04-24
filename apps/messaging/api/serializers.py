from rest_framework import serializers
from apps.messaging.models import MessageModel

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModel 
        fields = ["sender", "reciever", "content"]
        