"""
Functions for the view code
"""

from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import NurseProfile
from .forms import SubmitNurseProfile


class NursePage(generic.ListView):
    """
    view for nurse profile page
    """
    model = NurseProfile
    queryset = NurseProfile.objects.filter(status=1).order_by('-created_on')
    template_name = 'nurseprofile.html'
    paginate_by = 6


def submit_profile(request):
    """
    view for nurse profile submit page
    """
    if request.method == 'POST':
        profile_form = SubmitNurseProfile(request.POST, request.FILES)
        if profile_form.is_valid():
            profile_form.instance.print_name = request.user
            profile_form.save()
            messages.success(
                request, "Verifing your details! Check back soon.")
            return redirect('nurseprofile')
        else:
            profile_form = SubmitNurseProfile()

    return render(
        request,
        'submitprofile.html',
        {
            'profile_form': SubmitNurseProfile(),
        },
    )


def edit_profile(request):
    """
    Edit a nurse profile
    """
    profile = get_object_or_404(NurseProfile)
    form_edit = SubmitNurseProfile(request.POST or None, instance=profile)
    context = {
        'profile': profile,
        'form_edit': form_edit
    }

    if request.method == 'POST':
        form_edit = SubmitNurseProfile(
            request.POST, request.FILES, instance=profile
        )
        if form_edit.is_valid():
            profile = form_edit.save(commit=False)
            profile.nurse_name = request.User
            profile.save()
            return redirect('nurseprofile')
        else:
            form_edit = SubmitNurseProfile(instance=profile)

        return render(request, 'editnurseprofile.html', context)


def delete_profile(request):
    """
    Delete a nurse profile
    """
    profile = get_object_or_404(NurseProfile)
    profile.delete()
    return redirect('nurseprofile')


def nurse_details(request, primary_key):
    details = get_object_or_404(NurseProfile, pk=primary_key)
    return render(
        request=request,
        template_name='nursedetails.html',
        context={'details': details}
    )
