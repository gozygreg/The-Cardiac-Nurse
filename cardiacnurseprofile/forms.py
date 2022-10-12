"""
create a form that allow nurses
with registred account to submit their profile
"""
from django import forms
from .models import NurseProfile


class SubmitNurseProfile(forms.ModelForm):
    """
    Form for nurses to submit their profile
    """
    class Meta:
        """
        Fields to be displayed in profile form
        """
        model = NurseProfile
        fields = (
            'nurse_name',
            'specialty',
            'description',
            'nurse_image',
            'slug',
        )
        labels = {
            'nurse_name': 'Name',
            'specialty': 'Area of interest / Specialty',
            'description': 'Career Journey',
            'nurse_image': 'Profile picture',
            'slug': 'Repeat name',
        }
