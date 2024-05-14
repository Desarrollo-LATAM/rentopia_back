from rest_framework.routers import DefaultRouter

from apps.owners.api.viewsets import OwnerModelViewSet

routers = DefaultRouter()
routers.register(r"owners", OwnerModelViewSet, basename="owner")
urlpatterns = routers.urls
