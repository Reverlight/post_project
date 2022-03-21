from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .decorators import update_last_request, login_required
from .models import User, Post
from .renderers import UserJSONRenderer
from .serializers import UserSignupSerializer, UserLoginSerializer, UserSerializer
from .services import decode_token
from .forms import PostForm, UserForm


def main(request):
    return HttpResponse('<h1>Future Main</h1>')


def signup(request):
    form = UserForm()
    context = {'form': form}
    return render(request, 'post_app/user_signup.html', context)


class SignupAPIView(APIView):
    permission_classes = (AllowAny, )
    serializer_class = UserSignupSerializer

    def post(self, request):
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny, )
    renderer_classes = (UserJSONRenderer, )
    serializer_class = UserLoginSerializer

    @update_last_request
    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer_data = serializer.data

        response = Response()
        response.set_cookie(key='token', value=serializer_data['token'])
        response.data = serializer_data
        response.status_code = 200

        return response


class UserAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer
    renderer_classes = (UserJSONRenderer,)

    @update_last_request
    def get(self, request):
        token = request.COOKIES.get('token')
        payload = decode_token(token)

        user = User.objects.filter(id=payload['id']).first()
        serializer = self.serializer_class(user)

        return Response(serializer.data)


def analytics(request):
    return HttpResponse('<h1>Future Analytics</h1>')


class PostList(ListView):
    template_name = 'post_app/post_listing.html'
    model = Post


class PostCreate(CreateView):
    @login_required
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
            return HttpResponse('<h1>Form is saved!</h1>', status=200)
        return render(request, 'post_app/post_form.html', {'form', form})


def like(request):
    return HttpResponse('<h1>Future Post Like</h1>')
