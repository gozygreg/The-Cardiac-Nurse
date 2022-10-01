from django.shortcuts import render, get_object_or_404
from django.views import generic, View
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


class BlogPostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = NurseBlog.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'blogpost_detail.html',
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )
