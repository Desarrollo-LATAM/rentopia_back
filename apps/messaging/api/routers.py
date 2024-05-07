from rest_framework.routers import DefaultRouter

from apps.messaging.api.viewsets import MessageViewSet

router = DefaultRouter()
router.register(r'mensajes', MessageViewSet,  basename='messages')


urlpatterns = router.urls

