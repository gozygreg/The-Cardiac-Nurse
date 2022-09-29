from django.shortcuts import render
from django.views import generic
from .models import NurseBlog



class BlogPage(generic.ListView):
    """
    view for blog page
    """
    model = NurseBlog
    # content of NurseBlog table
    queryset = NurseBlog.objects.filter(status=1).order_by('-created_on')
    # HTML file for view to render
    template_name = 'nurseblog.html'
    # Limit number of blog post that appear on front page to 6
    paginate_by = 6
