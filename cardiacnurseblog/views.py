"""
Functions for the view code
"""
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import NurseBlog
from .forms import BlogCommentForm


def home_page(request):
    """
    view for home page.
    """
    return render(request, 'index.html')


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
                "commented": False,
                "liked": liked,
                "comment_form": BlogCommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = NurseBlog.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = BlogCommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = BlogCommentForm()

        return render(
            request,
            "blogpost_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )
