from . import views
from django.urls import path


urlpatterns = [
    path('', views.home_page, name='home'),
    path('nurseblog/', views.BlogPage.as_view(), name='our_blog'),
    path('<slug:slug>/', views.BlogPostDetail.as_view(), name='blogpost_detail'),
]