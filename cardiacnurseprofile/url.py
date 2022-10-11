from . import views
from django.urls import path


urlpatterns = [
    path('nurseprofile/', views.NursePage.as_view(), name='nurse_profile')
]