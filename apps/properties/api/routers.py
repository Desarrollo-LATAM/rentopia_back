from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.properties.api import (
    ApartmentViewSet,
    HouseViewSet,
    LandViewSet,
    PropertyViewSet,
)

router = DefaultRouter()
router.register(r"properties", PropertyViewSet, basename="properties")
router.register(r"apartments", ApartmentViewSet, basename="apartments")
router.register(r"lands", LandViewSet, basename="lands")
router.register(r"houses", HouseViewSet, basename="houses")

urlpatterns = [path("", include(router.urls))]
