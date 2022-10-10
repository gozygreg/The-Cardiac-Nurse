"""
Database models for nurse profile pagw
"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


# class Specialty(models.Model):
#     """
#     Nurses' area of specialty
#     or area of interest
#     """
#     choice = ((1, 'IHD'), (2, 'HF'), (3, 'CCU'))

#     specialty = models.CharField(
#         max_length=50, choices=choice, null=True, blank=True)

#     class Meta:
#         """
#         Display order
#         """
#         ordering = ('specialty',)

#     def __str__(self):
#         """
#         Display order
#         """
#         return self.specialty


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
    # specialty = models.ForeignKey(
    #     Specialty, on_delete=models.PROTECT, blank=False, null=False)
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
