from django.db import models

from apps.abstracts.models import AbstractModel
from apps.users.models import User

# Create your models here.

PROPERTY_TYPE_CHOICES = {
    "AP": "Apartment",
    "LA": "Land",
    "HO": "House",
}


class Property(AbstractModel):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='owner') 
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.PositiveIntegerField()
    num_bedrooms = models.PositiveIntegerField()
    num_bathrooms = models.PositiveIntegerField()
    property_type = models.CharField(
        max_length=2,
        choices=PROPERTY_TYPE_CHOICES,
        blank=False,
    )
    rating_property = models.PositiveIntegerField(default=0)


class Apartment(Property):
    num_floors = models.PositiveIntegerField()


class Land(Property):
    area = models.DecimalField(max_digits=10, decimal_places=2)


class House(Property):
    num_floors = models.PositiveIntegerField()
