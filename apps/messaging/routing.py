from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from apps.messaging.consumers import ChatConsumer

# TODO: Chequear porque no toma los imports de channels y chequear si estan bien ubicados los archivos routing y consumers. También chequear si debo hacer de routers y routing un solo archivo


application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/mensajes/<str:receiver_name>/', ChatConsumer.as_asgi()),
        ])
    ),
})
