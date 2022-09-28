"""
Database models for the Nurseblog app
"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Idea for this model was from 'I think therefore I blog' walkthrough project


class NurseBlog(models.Model):
    """
    Database for submitting a blog post
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="nurse_blog"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        """
        To display blog post in desending order
        """
        ordering = ["-created_on"]

    def __str__(self):
        """
        To display a string representation of an object
        """
        return self.title

    def number_of_likes(self):
        """
        To return total number of likes on a post
        """
        return self.likes.count()


class BlogComment(models.Model):
    """
    Database models to create comment for the nurseblog
    """

    post = models.ForeignKey(NurseBlog, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        To arrange comments in asending order
        """
        ordering = ["created_on"]

    def __str__(self):
        """
        To display the comment as the comment text,
        and the name of the comment author
        """
        return f"Comment {self.body} by {self.name}"
