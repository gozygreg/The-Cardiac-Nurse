"""
Database models for nurse profile page
"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class NurseProfile(models.Model):
    """
    Database model for nurse profile
    """
    choice = ((1, 'Ischemic Heart Disease'), (
        2, 'Heart Failure'), (3, 'Coronary Care'), (
            4, 'Arrythmia'), (5, 'Congenital Heart Disease'), (
                6, 'Other'))

    specialty = models.IntegerField(choices=choice, null=True, blank=True)
    nurse_name = models.CharField(
        max_length=50, unique=True, null=False, blank=False)
    slug = models.SlugField(
        max_length=50, unique=True, null=False, blank=False)
    description = models.TextField()
    nurse_image = CloudinaryField('image', null=False, blank=False)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        To display the most recently
        nurse on the platform
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Display the name of nurse
        instead of the model ID
        """
        return self.nurse_name
