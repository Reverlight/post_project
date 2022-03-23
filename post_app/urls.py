from django.urls import path

from .views.api import (
    SignupAPIView,
    UserAPIView,
    like_api,
    LoginAPIView,
)
from .views.pages import (
    PostList,
    PostCreate,
    PostDetail,
    signup,
    login,
    analytics,
    main
)

urlpatterns = [
    path('', main, name='main'),
    path('user/signup/api/', SignupAPIView.as_view(), name='signup-api'),
    path('user/signup/', signup, name='signup'),
    path('user/login/', login, name='login'),
    path('user/', UserAPIView.as_view(), name='user'),
    path('user/login/api/', LoginAPIView.as_view(), name='login-api'),
    path('post/creation/', PostCreate.as_view(), name='creation'),
    path('post/<int:pk>/', PostDetail.as_view(), name='detail'),
    path('post/<int:pk>/like/', like_api, name='like'),
    path('posts/', PostList.as_view(), name='posts'),
    path('analytics/', analytics, name='analytics')
]