from django.urls import path
from main_blog.views import blog_home, blog_post_detail, search_posts, list_posts_by_tag
urlpatterns = [
    path('', blog_home, name='blog_home'),
    path('search_posts/',search_posts, name='search'),
    path('post/<slug:slug>/',blog_post_detail, name='blog_post_detail'),
    path("tags/<slug:slug>",list_posts_by_tag, name="tag")
]
