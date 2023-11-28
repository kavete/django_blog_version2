# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .forms import SubscriberForm
# from main_blog.forms import PostForm
from .models import BlogPost, Tag
from django.db.models import Q


def blog_home(request):
    all_posts = BlogPost.objects.all().order_by("-date_published")
    paginator = Paginator(all_posts, per_page=2)
    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)
    context = {
        "all_posts": data,
    }
    return render(request, "home.html", context)


def search_posts(request):
    search_word = request.GET["search_word"]
    if not search_word == "":
        all_posts = BlogPost.objects.filter(
            Q(title__icontains=search_word)
            | Q(author__first_name__icontains=search_word)
            | Q(author__last_name__icontains=search_word) |
            Q(content__icontains=search_word)
        )
        paginator = Paginator(all_posts, per_page=2)
        page_number = request.GET.get("page")
        data = paginator.get_page(page_number)
        # TODO Use Elastic search instead
        return render(request, "home.html", {"all_posts": data})
    else:
        return redirect("blog_home")


def blog_post_detail(request, slug):
    post = BlogPost.objects.get(slug=slug)
    random_posts = BlogPost.objects.order_by("?")[:5]
    post_tags = post.tags.all()
    related_posts = (
        BlogPost.objects.filter(tags__in=post_tags).exclude(slug=slug).distinct()[:5]
    )
    context = {
        "blog_post": post,
        "random_posts": random_posts,
        "related_posts": related_posts,
    }
    return render(request, "blog_details.html", context)


def list_posts_by_tag(request, slug):
    tag = Tag.objects.get(slug=slug)
    posts = BlogPost.objects.filter(tags=tag)

    context = {"all_posts": posts}

    return render(request, "home.html", context)


# @login_required
# def create_post(request):
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Post Created successfully")
#         else:
#             messages.error(request, "Please enter valid values")
#             return redirect("create_post")
#     else:
#         form = PostForm()
#     return render(request, "create_post.html", {"post_form": form})


def subscribe(request):
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for subscribing")
            return redirect(request.META.get('HTTP_REFERER', 'blog_home'))
        else:
            messages.error(request, "You could not be added to the subscription list")
            return redirect(request.META.get('HTTP_REFERER', 'blog_home'))
    else:
        subscription_form = SubscriberForm()

    return redirect(request.META.get('HTTP_REFERER', 'blog_home'))
