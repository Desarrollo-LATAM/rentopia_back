from rest_framework import serializers

from apps.properties.models import Apartment, House, Land, Property


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = "__all__"


class ApartmentSerializer(PropertySerializer):
    class Meta(PropertySerializer.Meta):
        model = Apartment
        fields = PropertySerializer.Meta.fields + ["num_floors"]


class LandSerializer(PropertySerializer):
    class Meta(PropertySerializer.Meta):
        model = Land
        fields = PropertySerializer.Meta.fields + ["area"]


class HouseSerializer(PropertySerializer):
    class Meta(PropertySerializer.Meta):
        model = House
        fields = PropertySerializer.Meta.fields + ["num_floors"]
