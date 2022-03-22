from django.http import HttpResponse
from django.shortcuts import render

from ..forms import UserForm, UserLoginForm


def analytics(request):
    return HttpResponse('<h1>Future Analytics</h1>')


def main(request):
    return HttpResponse('<h1>Future Main</h1>')


def signup(request):
    form = UserForm()
    context = {'form': form}
    return render(request, 'post_app/user_signup.html', context)


def login(request):
    form = UserLoginForm()
    context = {'form': form}
    return render(request, 'post_app/user_login.html', context)
