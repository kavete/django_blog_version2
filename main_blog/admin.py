from django.contrib import admin
from .models import BlogPost, Subscriber, Tag

admin.site.site_header = "Kavete's Blog"
admin.site.index_title = "Management"


# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date_published")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "author", "content")
    ordering = ("-date_published",)


class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("name",)


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Tag, TagAdmin)


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'name']
    search_fields= ['email', 'name']

admin.site.register(Subscriber, SubscriberAdmin)