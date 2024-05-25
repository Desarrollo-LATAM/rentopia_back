from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.messaging.api.viewsets import MessageViewSet

router = DefaultRouter()
router.register(r'messages', MessageViewSet,  basename='message')


urlpatterns = [path("", include(router.urls))]

