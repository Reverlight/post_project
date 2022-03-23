from django import forms
from django.forms import ModelForm

from .models import Post, User


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']


class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']


class UserSignupForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            data = {
                'class': 'form-control',
                'placeholder': f'Enter {str(field)}'
            }
            self.fields[str(field)].widget.attrs.update(data)
