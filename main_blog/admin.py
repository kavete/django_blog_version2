from django.contrib import admin
from .models import BlogPost, Subscriber, Tag

#  Admin customizations
admin.site.site_header = "Teensci"
admin.site.index_title = "Management"


# Blogpost model admin customization
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date_published", "featured")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ["author", "date_published"]
    search_fields = ("title", "author", "content")
    ordering = ("-date_published",)


# Tag model admin customizations
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("name",)


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Tag, TagAdmin)


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'name']
    search_fields = ['email', 'name']


admin.site.register(Subscriber, SubscriberAdmin)
