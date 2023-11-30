import uuid
import os
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


def unique_image_name(instance, filename):
    name = uuid.uuid4()
    extension = filename.split(".")[-1]
    fullname = f"{name}.{extension}"
    return os.path.join("blog_post_images", fullname)


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return f"{self.name}"


class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    prepopulated_fields = {"slug": ("firstname", "lastname")}
    preview_image = models.ImageField(
        upload_to=unique_image_name, null=True, blank=True
    )
    tags = models.ManyToManyField(to=Tag, related_name="posts", blank=True)
    slug = models.SlugField(default="", null=False, unique=True)
    content = RichTextUploadingField(null=False)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} by {self.author}"


class Subscriber(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
