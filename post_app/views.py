from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    return HttpResponse('<h1>Future Main</h1>')


def signup(request):
    return HttpResponse('<h1>Future Sign up</h1>')


def login(request):
    return HttpResponse('<h1>Future Login</h1>')


def analytics(request):
    return HttpResponse('<h1>Future Analytics</h1>')


def creation(request):
    return HttpResponse('<h1>Future Post Creation</h1>')


def like(request):
    return HttpResponse('<h1>Future Post Like</h1>')