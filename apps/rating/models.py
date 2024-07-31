# rating/models.py
from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Review(models.Model):
    RATING_CHOICES = [(i, i) for i in range(1, 6)]

    owner = models.ForeignKey(User, related_name='owner_reviews', on_delete=models.CASCADE)
    tenant = models.ForeignKey(User, related_name='tenant_reviews', on_delete=models.CASCADE)
    property = models.ForeignKey(Property, related_name='property_reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner} - {self.property} - {self.rating}'