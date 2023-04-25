from django.test import TestCase, Client
from django.urls import reverse
from .models import NurseBlog
from .view import home_page


class BlogPageTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page(self):
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
