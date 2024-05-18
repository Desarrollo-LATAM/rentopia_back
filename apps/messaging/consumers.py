import json

from channels.generic.websocket import AsyncWebsocketConsumer

from apps.properties.models import Property


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.sender = self.scope['user']  # Obtener el usuario que inicia la conexión
        self.property_id = self.scope['url_route']['kwargs']['property_id'] # Obtener el ID de la propiedad desde la URL

        try:
            self.property = Property.objects.get(id=self.property_id)
            self.receiver = self.property.owner  # Obtener el usuario propietario de la propiedad

            # Generar el nombre de la sala utilizando el ID de la propiedad
            self.room_name = f"property_{self.property_id}"

            # Unirse a la sala
            await self.channel_layer.group_add(
                self.room_name,
                self.channel_name
            )

            await self.accept()
        except Property.DoesNotExist:
            await self.close()

    async def disconnect(self, close_code):
        # Dejar la sala
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_content = text_data_json['message_content']

        # Enviar el mensaje a la sala
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'chat_message',
                'message_content': message_content,
                'sender': self.sender.username
            }
        )

    async def chat_message(self, event):
        message_content = event['message_content']
        sender = event['sender']

        # Enviar el mensaje al WebSocket
        await self.send(text_data=json.dumps({
            'message_content': message_content,
            'sender': sender
        }))


