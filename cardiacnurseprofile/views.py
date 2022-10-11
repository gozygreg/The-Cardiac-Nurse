"""
Functions for the view code
"""

from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from . models import NurseProfile


class NursePage(generic.ListView):
    """
    view for nurse profile page
    """
    model = NurseProfile
    queryset = NurseProfile.objects.filter(status=1).order_by('-created_on')
    template_name = 'nurseprofile.html'
    paginate_by = 6
