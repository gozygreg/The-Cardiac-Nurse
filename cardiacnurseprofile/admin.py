"""
Providing access to NurseProfile in
the admin panel of django
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from . models import NurseProfile


@admin.register(NurseProfile)
class NurseProfileAdmin(SummernoteModelAdmin):
    """
    To control or manage how details are dispayed
    on django admin panel
    """
    # prepopulated_fields = {'slug': ('nurse_name',)}
    list_display = ('nurse_name', 'specialty', 'status')
    list_filter = ('specialty', 'created_on')
    search_fields = ('nurse_name', 'specialty')
    actions = ['verify_nurse']
    summernote_fields = ('description')
    fields = ('nurse_name', 'specialty', 'description', 'nurse_image',)

    def verify_nurse(self, request, queryset):
        """
        Function to verify nurse wanting
        to join the platform
        """
        queryset.update(status=1)
