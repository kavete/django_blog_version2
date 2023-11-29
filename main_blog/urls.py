from django.urls import path

from main_blog.views import blog_home, blog_post_detail, search_posts, list_posts_by_tag, subscribe, signup, signout, \
    signin

urlpatterns = [
    path('', blog_home, name='blog_home'),
    path('search_posts/', search_posts, name='search'),
    path('post/<slug:slug>/', blog_post_detail, name='blog_post_detail'),
    path("tag/<slug:slug>", list_posts_by_tag, name="tag"),
    path('subscribe/', subscribe, name='subscribe'),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('signout/', signout, name='signout'),
]
