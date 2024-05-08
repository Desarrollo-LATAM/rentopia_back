from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from apps.messaging.consumers import ChatConsumer

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/api/messages/<str:receiver_username>/', ChatConsumer.as_asgi()),
        ])
    ),
})


