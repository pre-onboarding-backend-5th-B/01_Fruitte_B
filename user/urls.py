from django.urls import path
from .views import UserJoinApiView, UserLoginApiView

urlpatterns = [
    path("join/", UserJoinApiView.as_view()),
    path("login/", UserLoginApiView.as_view()),
]
