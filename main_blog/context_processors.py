import os
import uuid

from django.contrib import messages
from django.shortcuts import redirect, render

from main_blog.forms import SubscriberForm
from main_blog.models import Tag


def get_all_tags(request):
    all_tags = Tag.objects.all().order_by("?")[:10]
    return {"all_tags": all_tags}


def subscription_form(request):
    form = SubscriberForm()
    return {'subscription_form': form}

# def subscribe(request):
#     if request.method == "POST":
#         form = SubscriberForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Thank you for subscribing")
#             return redirect(request.META.get('HTTP_REFERER', 'blog_home'))
#         else:
#             messages.error(request, "You could not be added to the subscription list")
#             return redirect(request.META.get('HTTP_REFERER', 'blog_home'))
#     else:
#         form = SubscriberForm()
#         context = {
#             'sub_form': form
#         }
#
#     return redirect(request.META.get('HTTP_REFERER', 'blog_home'))


# def unique_editor_uploads(instance, filename):
#     name = uuid.uuid4()
#     extension = filename.split(".")[-1]
#     fullname = f"{name}.{extension}"
#     return os.path.join("uploads", fullname)
