from django import forms

from .models import BlogPost, Subscriber


# from ckeditor.widgets import CKEditorWidget

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email', 'name']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Your email'}),
            'name': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Your name'}),
        }


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = BlogPost
#         fields = ['title', 'author', 'preview_image', 'tags', 'slug', 'content']
#         # content = forms.CharField(widget=CKEditorWidget())
#
#         # widgets = {
#         #     'title': forms.TextInput(attrs={'class':'form-control mb-3'}),
#         #     'author': forms.SelectMultiple(attrs={'class': 'mb-3'}),
#         #     'preview_image': forms.FileInput(attrs={'class': 'mb-3'}),
#         #     'tags': forms.TextInput(attrs={'class': 'form-control mb-3'}),
#         #     'slug': forms.TextInput(attrs={'classs': 'form-control mb-3'}),
#         #     'content': forms.Textarea(attrs={'class': 'form-control mb-3', 'style': 'display:block !important;'},),
#         # }
