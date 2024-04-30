from django.urls import path, include
from rest_framework.routers import DefaultRouter
from properties.api import PropertyViewSet, LandViewSet, ApartmentViewSet, HouseViewSet

router = DefaultRouter()
router.register(r'properties', PropertyViewSet)
router.register(r'apartments', ApartmentViewSet)
router.register(r'lands', LandViewSet)
router.register(r'houses', HouseViewSet) 

urlpatterns = [
    path('', include(router.urls))
]