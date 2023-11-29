from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Subscriber


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email', 'name']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Your email'}),
            'name': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Your name'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
