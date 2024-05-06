from rest_framework import serializers

from apps.owners.models import Owner


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = "__all__"
