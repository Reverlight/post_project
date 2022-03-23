from django.http import JsonResponse, HttpResponseNotFound
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Post, User
from ..renderers import UserJSONRenderer
from ..serializers import UserSignupSerializer, UserLoginSerializer, UserSerializer
from ..services import decode_token


def like_api(request, **kwargs):
    if request.method == 'POST':
        token = request.COOKIES.get('token')
        payload = decode_token(token)
        user = User.objects.filter(id=payload['id']).first()
        post = Post.objects.filter(id=kwargs['pk']).first()

        if not post.has_user_liked(user):
            post.set_like(user)
            return JsonResponse({'status': 'like_set'})
        else:
            post.set_dislike(user)
            return JsonResponse({'status': 'dislike_set'})
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')


class SignupAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSignupSerializer

    def post(self, request):
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserLoginSerializer

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
    serializer_class = UserSerializer
    renderer_classes = (UserJSONRenderer,)

    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)
