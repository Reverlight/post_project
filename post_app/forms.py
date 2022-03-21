from django.forms import ModelForm

from .models import Post, User


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']