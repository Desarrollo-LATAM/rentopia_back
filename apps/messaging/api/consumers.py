import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User

# TODO: Chequear porque no toma los imports de channels


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.sender = self.scope['user']  # Obtener el usuario que inicia la conexión
        self.receiver_name = self.scope['url_route']['kwargs']['receiver_name']
        self.receiver = User.objects.get(username=self.receiver_name)  # Obtener el usuario destinatario

        # Generar el nombre de la sala utilizando los nombres de usuario de ambos usuarios
        self.room_name = f"{self.sender.username}_{self.receiver.username}"

        # Unirse a la sala
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Dejar la sala
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Enviar el mensaje a la sala
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']

        # Enviar el mensaje al WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
