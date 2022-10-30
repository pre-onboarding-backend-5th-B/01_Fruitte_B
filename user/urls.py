from django.urls import path
from .views import UserJoinApiView, UserLoginApiView, UserLogoutApiView, UserApiView

urlpatterns = [
    path("", UserApiView.as_view()),
    path("join/", UserJoinApiView.as_view()),
    path("login/", UserLoginApiView.as_view()),
    path("logout/", UserLogoutApiView.as_view()),
]
