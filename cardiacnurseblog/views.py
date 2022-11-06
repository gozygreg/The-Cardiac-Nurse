"""
Functions for the view code
"""
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import NurseBlog
from .forms import BlogCommentForm


def home_page(request):
    """
    view for home page.
    """
    return render(request, 'index.html')


# Class used from 'I think before I blog' walkthrough project
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


# Class used from 'I think before I blog' walkthrough project
class BlogPostDetail(View):
    """
    To allow individual blog post
    to be rendered on a webpage for more detail
    about the particular blog post
    """
    def get(self, request, slug, *args, **kwargs):
        """
        creates a comment session
        on a page
        """
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
        """
        allows users to submit
        new comments to a blog post
        """
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


# Class used from 'I think before I blog' walkthrough project
class BlogPostLike(View):
    """
    lets user like a blog post
    """
    def post(self, request, slug):
        """
        checks for user
        """
        post = get_object_or_404(NurseBlog, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('blogpost_detail', args=[slug]))
