"""
Database models for nurse profile pagw
"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Specialty(models.Model):
    """
    Nurses' area of specialty
    or area of interest
    """
    specialty = models.CharField(max_length=50)

    class Meta:
        """
        Display order
        """
        ordering = ('specialty',)

    def __str__(self):
        """
        Display order
        """
        return self.specialty


class NurseProfile(models.Model):
    nurse_name = models.CharField(
        max_length=50, unique=True, null=False, blank=False)
    slug = models.SlugField(
        max_length=50, unique=True, null=False, blank=False)
    specialty = models.ForeignKey(
        Specialty, on_delete=models.PROTECT, blank=False, null=False)
    description = models.TextField()
    nurse_image = CloudinaryField('image', null=False, blank=False)
    status = models.IntegerField(null=False, blank=False)
    year_qualified = models.IntegerField(null=False, blank=False)
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
