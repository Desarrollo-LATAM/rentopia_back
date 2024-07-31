# rating/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Property, Review
from rest_framework.test import APIClient

class ReviewAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.owner = User.objects.create_user(username='owner', password='password')
        self.tenant = User.objects.create_user(username='tenant', password='password')
        self.property = Property.objects.create(name='Test Property', description='Test Description')
        self.review = Review.objects.create(
            owner=self.owner,
            tenant=self.tenant,
            property=self.property,
            rating=5,
            comment='Great!'
        )

    def test_create_review(self):
        data = {
            'owner': self.owner.id,
            'tenant': self.tenant.id,
            'property': self.property.id,
            'rating': 4,
            'comment': 'Good'
        }
        response = self.client.post('/api/reviews/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['rating'], 4)
        self.assertEqual(response.data['comment'], 'Good')

    def test_get_reviews(self):
        response = self.client.get('/api/reviews/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['comment'], 'Great!')