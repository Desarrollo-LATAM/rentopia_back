from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from apps.messaging.consumers import ChatConsumer

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/mensajes/<str:receiver_name>/', ChatConsumer.as_asgi()),
        ])
    ),
})


# TODO: Chequear si estan bien ubicados los archivos routing y consumers. También chequear si debo hacer de routers y routing un solo archivo
