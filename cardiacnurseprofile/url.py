from django.urls import path
from . import views


urlpatterns = [
    path('nurseprofile/', views.NursePage.as_view(), name='nurse_profile'),
    path('submitprofile/', views.submit_profile, name='submitprofile'),
    path('edit/<slug:slug>', views.edit_profile, name='editnurseprofile'),
    path('delete/<slug:slug>', views.delete_profile, name='deleteprofile'),
    path('<slug:slug>/', views.NurseDetails.as_view(), name='nursedetails'),
]
