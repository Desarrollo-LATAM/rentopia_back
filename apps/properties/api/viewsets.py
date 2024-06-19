from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from apps.properties.models import Apartment, House, Land, Property

from .serializers import (
    ApartmentSerializer,
    HouseSerializer,
    LandSerializer,
    PropertySerializer,
)

class CustomPagination(PageNumberPagination):
    page_size = 10  
    max_page_size = 20  
    page_size_query_param = 'page_size'  
    max_page_size_query_param = 'max_page_size'

    def get_paginated_response(self, data):

        return Response({
            'count': self.page.paginator.count,
            'num_pages': self.page.paginator.num_pages,
            'page_number': self.page.number,
            'page_size': self.page_size,
            'next_link': self.get_next_link(),
            'previous_link': self.get_previous_link(),
            'results': data
        })

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'location', 'price', 'property_type']

    pagination_class = CustomPagination

    filterset_fields = {
    'price': ['lte', 'gte'],       
}




class LandViewSet(viewsets.ModelViewSet):
    queryset = Land.objects.all()
    serializer_class = LandSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'location', 'price', 'property_type']

    pagination_class = CustomPagination

    filterset_fields = {
    'price': ['lte', 'gte'],       
}


class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'location', 'price', 'property_type']

    pagination_class = CustomPagination

    filterset_fields = {
    'price': ['lte', 'gte'],       
}


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'location', 'price', 'property_type']

    pagination_class = CustomPagination

    filterset_fields = {
    'price': ['lte', 'gte'],       
<<<<<<< Updated upstream
}
=======
}
>>>>>>> Stashed changes
