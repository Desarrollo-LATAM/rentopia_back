from rest_framework import viewsets, filters

from apps.properties.models import Apartment, House, Land, Property

from .serializers import (
    ApartmentSerializer,
    HouseSerializer,
    LandSerializer,
    PropertySerializer,
)


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'location', 'price', 'property_type']


class LandViewSet(viewsets.ModelViewSet):
    queryset = Land.objects.all()
    serializer_class = LandSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'location', 'price', 'property_type']


class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'location', 'price', 'property_type']


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'location', 'price', 'property_type']
