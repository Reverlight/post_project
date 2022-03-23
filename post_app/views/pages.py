from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from ..forms import UserSignupForm, UserLoginForm, PostForm
from ..models import Like, Post, User
from ..services import parse_date, decode_token


def analytics(request):
    _from = request.GET.get('date_from')
    _to = request.GET.get('date_to')

    if not _from or not _to:
        return HttpResponse(f'<h1>Please specify params date_from, date_to</h1>')

    date_from = parse_date(request.GET.get('date_from'))
    date_to = parse_date(request.GET.get('date_to'))

    r = Like.objects.filter(made_at_time__range=(date_from, date_to)).count()
    return HttpResponse(f'<h1>Future Analytics</h1> {r}')


def main(request):
    return render(request, 'post_app/url-guide-page.html')


def signup(request):
    form = UserSignupForm()
    context = {'form': form}
    return render(request, 'post_app/user_signup.html', context)


def login(request):
    form = UserLoginForm()
    context = {'form': form}
    return render(request, 'post_app/user_login.html', context)


class PostList(ListView):
    template_name = 'post_app/post_listing.html'
    model = Post
    context_object_name = 'posts'


class PostDetail(LoginRequiredMixin,DetailView):
    template_name = 'post_app/post_detail.html'
    model = Post
    context_object_name = 'post'


class PostCreate(LoginRequiredMixin, CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': PostForm()}
        return render(request, 'post_app/post_form.html', context)

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            token = request.COOKIES.get('token')
            payload = decode_token(token)

            user = User.objects.filter(id=payload['id']).first()
            post = form.save(commit=False)
            post.created_by = user
            post.save()

            return redirect(reverse('detail', kwargs={'pk': post.pk}))

        return render(request, 'post_app/post_form.html', {'form', form})
