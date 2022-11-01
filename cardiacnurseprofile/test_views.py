"""
Tests for Views
"""
from django.test import TestCase


# Test taken from "Hello Django" walkthrough project
class TestViews(TestCase):
    """
    Test views
    """
    def test_nurse_profile_page(self):
        """
        verify nurse profile page loads
        """
        response = self.client.get('/nurseprofile', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nurseprofile.html')
