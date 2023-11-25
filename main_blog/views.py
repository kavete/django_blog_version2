import django
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Tag
from django.db.models import Q
from .forms import SubscriberForm
# Configure Django
django.setup()


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
    all_posts = BlogPost.objects.filter(
        Q(title__icontains=search_word)
        | Q(author__first_name__icontains=search_word)
        | Q(author__last_name__icontains=search_word)
    )
    paginator = Paginator(all_posts, per_page=10)
    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)
    # TODO Use Elastic search instead
    return render(request, "home.html", {"all_posts": data})


def blog_post_detail(request, slug):
    post = BlogPost.objects.get(slug=slug)
    random_posts = BlogPost.objects.order_by('?')[:5]
    post_tags = post.tags.all()
    related_posts = BlogPost.objects.filter(tags__in=post_tags).exclude(slug=slug).distinct()[:5]
    context = {
        "blog_post": post,
        "random_posts": random_posts,
        "related_posts": related_posts,
    }
    return render(request, "blog_details.html", context)


def list_posts_by_tag(request, slug):

    # tag = get_object_or_404(Tag, slug=slug)
    tag = Tag.objects.get(slug=slug)
    posts = BlogPost.objects.filter(tags=tag)
    # posts = BlogPost.objects.filter(slug=tag)

    context = {
        "all_posts": posts
    }

    return render(request, "home.html", context)


    
def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a success page
    else:
        form = SubscriberForm()

    return render(request, 'subscribe.html', {'form': form})
