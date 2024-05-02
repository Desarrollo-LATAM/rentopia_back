from rest_framework.routers import DefaultRouter

from apps.messaging.api.viewsets import MessageViewSet, UserViewSet

router = DefaultRouter()
router.register(r'mensajes', MessageViewSet,  basename='messages')
router.register(r'usuarios', UserViewSet,  basename='users')



urlpatterns = router.urls

