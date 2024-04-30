from db_connection import db
from django.db import models

# Create your models here.

properties_collection = db["properties"]


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Property(AbstractModel):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.PositiveIntegerField()
    num_bedrooms = models.PositiveIntegerField() 
    num_bathrooms = models.PositiveIntegerField()
    property_type = models.CharField(max_length=15)

class Apartment(Property):
    num_floors = models.PositiveIntegerField()

class Land(Property):
    area = models.DecimalField(max_digits=10, decimal_places=2)

class House(Property):
    num_floors = models.PositiveIntegerField()
