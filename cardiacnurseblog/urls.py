from . import views
from django.urls import path


urlpatterns = [
    path('', views.BlogPage.as_view(), name='home'),
    path('<slug:slug>/', views.BlogPostDetail.as_view(), name='blogpost_detail'),
]