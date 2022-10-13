from django.urls import path
from . import views


urlpatterns = [
    path('nurseprofile/', views.NursePage.as_view(), name='nurse_profile'),
    path('submitprofile/', views.submit_profile, name='submitprofile'),
    path('editnurseprofile/', views.edit_profile, name='editnurseprofile'),
]
