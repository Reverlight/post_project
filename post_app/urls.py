from django.urls import path

from .views import (
    signup,
    creation,
    like,
    analytics,
    login
)

urlpatterns = [
    path('user/signup/', signup),
    path('user/login/', login),
    path('post/creation/', creation),
    path('post/like/', like),
    path('analytics/', analytics)
]