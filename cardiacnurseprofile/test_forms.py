"""
Testing forms
"""
from django.test import TestCase
from .forms import SubmitNurseProfile


# Test derived from "Hello Django" walkthrough project.
class TestSubmitNurseProfile(TestCase):
    """
    Tests for Submit Nurse Profile Form
    """
    def test_nurse_name_required(self):
        """
        Verify nurse name is required
        """
        form = SubmitNurseProfile({'nurse_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('nurse_name', form.errors.keys())
        self.assertEqual(
            form.errors['nurse_name'][0], 'This field is required.')
