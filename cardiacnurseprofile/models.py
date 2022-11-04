"""
Database models for nurse profile page
"""
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField
from django.urls import reverse


STATUS = ((0, "Draft"), (1, "Published"))


class NurseProfile(models.Model):
    """
    Database model for nurse profile
    """
    choice = (('Ischemic Heart Disease', ('IHD')), (
        'Heart Failure', ('HF')), ('Coronary Care', ('CC')), (
            'Arrythmia', ('ARY')), ('Congenital Heart Disease', ('CHD')), (
                'Other', ('Other')))

    specialty = models.CharField(max_length=200, choices=choice, default='Heart Failure')
    nurse_name = models.CharField(
        primary_key=True, max_length=50, unique=True, null=False, blank=False)
    slug = models.SlugField(
        max_length=250, null=False, unique=True, blank=False)
    description = models.TextField()
    nurse_image = CloudinaryField('image', null=False, blank=False)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now=True)
    profile_owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='nurse_profile', default=None)

    def __str__(self):
        return self.nurse_name

    def get_absolute_url(self):
        return reverse("nursedetails", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nurse_name)
        return super().save(*args, **kwargs)

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

