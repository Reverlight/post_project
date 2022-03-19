from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSignupSerializer

def main(request):
    return HttpResponse('<h1>Future Main</h1>')


class SignupAPIView(APIView):
    permission_classes = (AllowAny, )
    serializer_class = UserSignupSerializer

    def post(self, request):
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

def login(request):
    return HttpResponse('<h1>Future Login</h1>')


def analytics(request):
    return HttpResponse('<h1>Future Analytics</h1>')


def creation(request):
    return HttpResponse('<h1>Future Post Creation</h1>')


def like(request):
    return HttpResponse('<h1>Future Post Like</h1>')