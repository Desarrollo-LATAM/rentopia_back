from rest_framework.routers import DefaultRouter

from apps.tenants.api.viewsets import TenantModelViewSet

routers = DefaultRouter()
routers.register(r"tenants", TenantModelViewSet, basename="tenant")
urlpatterns = routers.urls
