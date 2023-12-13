from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .forms import SubscriberForm, LoginForm, SignupForm
from .models import BlogPost, Tag, Subscriber
from django.db.models import Q
from .tasks import send_newsletter


def blog_home(request):
    featured_posts = BlogPost.objects.filter(featured=True).order_by("-date_published")
    random_posts = BlogPost.objects.order_by("?")[:5]
    all_posts = BlogPost.objects.all().order_by("-date_published")[:10]
    context = {
        "all_posts": all_posts,
        "featured_posts": featured_posts,
        "random_posts": random_posts
    }
    return render(request, "home.html", context)


def search_posts(request):
    search_word = request.GET.get("search_word", "")
    # if not search_word == "":
    all_posts = BlogPost.objects.filter(
        Q(title__icontains=search_word)
        | Q(author__first_name__icontains=search_word)
        | Q(author__last_name__icontains=search_word) |
        Q(content__icontains=search_word)
    ).distinct()
    paginator = Paginator(all_posts, per_page=10)
    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)
    context = {
        "all_posts": data,
        "search_word": search_word
    }
    return render(request, "home.html", context)


def blog_post_detail(request, slug):
    post = BlogPost.objects.get(slug=slug)
    random_posts = BlogPost.objects.exclude(slug=slug).order_by("?")[:5]
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
    posts = BlogPost.objects.filter(tags=tag).order_by('?')
    random_posts = BlogPost.objects.order_by("?")[:5]
    featured_posts = BlogPost.objects.filter(featured=True).order_by("-date_published")
    paginator = Paginator(posts, per_page=10)
    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)
    context = {"all_posts": data,
               "post_tag": tag,
               "random_posts": random_posts,
               "featured_posts": featured_posts
               }

    return render(request, "home.html", context)


def subscribe(request):
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        user_email = request.POST.get("email")
        email_exist = Subscriber.objects.filter(email=user_email)
        print(email_exist)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for subscribing")
            return redirect(request.META.get('HTTP_REFERER', 'blog_home'))
        elif email_exist:
            messages.error(request, "A user with this email already exists")
            return redirect(request.META.get('HTTP_REFERER', 'blog_home'))
        else:
            messages.error(request, "You could not be added to the subscription list")
            return redirect(request.META.get('HTTP_REFERER', 'blog_home'))
    return redirect(request.META.get('HTTP_REFERER', 'blog_home'))


def signin(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'login_form': form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'You are now logged in as {user.username}')
                return redirect('blog_home')

            else:
                messages.error(request, "Wrong username or password")
                return render(request, 'login.html', {'login_form': form})
        else:
            return render(request, 'login.html', {'login_form': form})


@login_required
def signout(request):
    logout(request)
    return redirect('signin')


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Successfully signed up as {user.username} ")
            return redirect('blog_home')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'signup_form': form})


def send_newsletter_view(request):
    subscribers = Subscriber.objects.all()

    for subscriber in subscribers:
        send_newsletter.delay(subscriber.email)

    return render(request, 'newsletter_sent.html')
