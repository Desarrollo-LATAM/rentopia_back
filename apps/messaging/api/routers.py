from django.urls import path
from apps.messaging.api.viewsets import MessageViewSet

urlpatterns = [
    path("mensajes/", MessageViewSet.as_view, name = "mensajes")
]

# TODO: Agregar las rutas al archivo urls.py general