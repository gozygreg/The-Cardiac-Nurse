"""
Tests for Views
"""
from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    """
    Test views
    """
    def test_nurse_profile_page(self):
        """
        verify nurse profile page loads
        """
        url = reverse('nurse_profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nurseprofile.html')
