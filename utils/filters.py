from django_filters import rest_framework

from apps.owners.models import Owner
from apps.tenants.models import Tenant
from apps.users.models import User


class UserFilterSet(rest_framework.FilterSet):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "is_owner",
        )


class OwnerFilterSet(rest_framework.FilterSet):
    class Meta:
        model = Owner
        fields = (
            "user_id",
            "name",
            "last_name",
            "rating_user",
        )
        ordering = ("created",)


class TenantFilterSet(rest_framework.FilterSet):
    class Meta:
        model = Tenant
        fields = (
            "user_id",
            "name",
            "last_name",
            "rating_user",
        )
        ordering = ("created",)
