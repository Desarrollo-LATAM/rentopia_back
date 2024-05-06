from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from apps.owners.api.serializers import OwnerSerializer
from apps.users.api import permissions
from utils.filters import OwnerFilterSet
from utils.pagination import ExtendedPagination


class OwnerModelViewSet(ModelViewSet):
    serializer_class = OwnerSerializer
    pagination_class = ExtendedPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_class = OwnerFilterSet
    permission_classes = [
        permissions.IsTenant | permissions.IsOwner | permissions.ReadOnly
    ]

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.order_by("last_name")
