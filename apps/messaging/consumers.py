import json

from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from django.db import close_old_connections

from apps.properties.models import Property

from .models import MessageModel

User = get_user_model()


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):        
        self.sender = self.scope['user']  # Obtener el usuario que inicia la conexión
        self.property_id = self.scope['url_route']['kwargs']['property_id'] # Obtener el ID de la propiedad desde la URL
        self.room_name = self.property_id
        self.room_group_name = f'chat_{self.room_name}'

        try:
            self.property = await database_sync_to_async(Property.objects.get)(id=self.property_id)
            # Obtener el propietario de manera asíncrona
            self.receiver = await sync_to_async(lambda: self.property.owner)()
            # Cerrar conexiones a la base de datos cuando se use sync_to_async
            await sync_to_async(close_old_connections)()
        
            # Generar el nombre de la sala utilizando el título de la propiedad
            self.room_name = self.property.title
                        
            # Unirse a la sala
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )

            await self.accept()            
            
        except Property.DoesNotExist:
            await self.close()


    async def disconnect(self, close_code):
        # Dejar la sala
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )


    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_content = text_data_json['message_content']
        sender_username = text_data_json['sender']

        
        # Buscar el usuario por su nombre de usuario
        sender = await sync_to_async(User.objects.get)(username=sender_username)

        # Guardar el mensaje en la base de datos
        await self.save_message(sender, message_content)

        # Enviar el mensaje a la sala
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message_content': message_content,
                'sender': sender_username
            }
        )


    async def chat_message(self, event):
        message_content = event['message_content']
        sender = event['sender']

        # Enviar el mensaje al WebSocket
        await self.send(text_data=json.dumps({
            'message_content': message_content,
            'sender': sender,
            'type': 'chat_message',
        }))

    @sync_to_async
    def save_message(self, sender, message_content):
        print(f'Guardando mensaje: {message_content} de {sender.username}')  # Mensaje de depuración
        MessageModel.objects.create(
            sender=sender,
            receiver=self.receiver,
            property=self.property, 
            message_content=message_content
        )




            # self.property = Property.objects.get(id=self.property_id)
# Generar el nombre de la sala utilizando el ID de la propiedad
            # self.room_name = f"Propiedad: {self.property_id}"
