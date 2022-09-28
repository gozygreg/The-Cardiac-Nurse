"""
Grants assess to Django admin panel
"""
from django.contrib import admin
from .models import NurseBlog, BlogComment
from django_summernote.admin import SummernoteModelAdmin


# Summernote idea and class inspired from 'I think therefore I blog'
@admin.register(NurseBlog)
class NurseBlogAdmin(SummernoteModelAdmin):
    """
    Using summernote text editor in Django admin panel for nurseblog
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    """
    For providing admin assess to manage comments
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        For approving pending user comments on blog post
        """
        queryset.update(approved=True)
