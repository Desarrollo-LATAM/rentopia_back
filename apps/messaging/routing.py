from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path

from apps.messaging.consumers import ChatConsumer

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            re_path(r'ws/api/messages/(?P<property_id>[^/]+)/$', ChatConsumer.as_asgi()),
        ])
    ),
})


