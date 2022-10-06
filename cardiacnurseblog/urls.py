"""
url paths for views to be rendered to the browser
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('nurseblog/', views.BlogPage.as_view(), name='our_blog'),
    path('<slug:slug>/', views.BlogPostDetail.as_view(), name='blogpost_detail'),
    path('like/<slug:slug>', views.BlogPostLike.as_view(), name='post_like'),
]
