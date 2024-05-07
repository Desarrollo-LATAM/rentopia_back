from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins
from rest_framework.viewsets import GenericViewSet

from apps.tenants.api.serializers import TenantSerializer
from apps.users.api import permissions
from utils.filters import TenantFilterSet
from utils.pagination import ExtendedPagination


class TenantModelViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):
    serializer_class = TenantSerializer
    pagination_class = ExtendedPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_class = TenantFilterSet
    permission_classes = [
        permissions.IsTenant | permissions.IsOwner | permissions.ReadOnly
    ]

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.order_by("last_name")
