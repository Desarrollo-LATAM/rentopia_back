"""
URL configuration for rentopia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from apps.messaging.api.viewsets import LoginViewSet, MessageViewSet, UserViewSet

router = DefaultRouter()
router.register(r'mensajes', MessageViewSet,  basename='messages')
router.register(r'usuarios', UserViewSet,  basename='users')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.messaging.api.routers')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('iniciar_sesion/', LoginViewSet.as_view({'post': 'iniciar_sesion'}), name='iniciar_sesion'),
]

urlpatterns += router.urls
