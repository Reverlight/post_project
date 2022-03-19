from django.urls import path

from .views import (
    SignupAPIView,
    creation,
    like,
    analytics,
    LoginAPIView,
    main
)

urlpatterns = [
    path('', main, name='main'),
    path('user/signup/', SignupAPIView.as_view(), name='signup'),
    path('user/login/', LoginAPIView.as_view(), name='login'),
    path('post/creation/', creation, name='creation'),
    path('post/like/', like, name='like'),
    path('analytics/', analytics, name='analytics')
]