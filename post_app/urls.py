from django.urls import path

from .views import (
    SignupAPIView,
    signup,
    login,
    UserAPIView,
    PostCreate,
    PostList,
    like,
    analytics,
    LoginAPIView,
    main
)

urlpatterns = [
    path('', main, name='main'),
    path('user/signup/api/', SignupAPIView.as_view(), name='signup-api'),
    path('user/signup/', signup, name='signup'),
    path('user/login/', login, name='login'),
    path('user/', UserAPIView.as_view(), name='user-data'),
    path('user/login/api/', LoginAPIView.as_view(), name='login-api'),
    path('post/creation/', PostCreate.as_view(), name='creation'),
    path('posts/', PostList.as_view(), name='creation'),
    path('post/like/', like, name='like'),
    path('analytics/', analytics, name='analytics')
]