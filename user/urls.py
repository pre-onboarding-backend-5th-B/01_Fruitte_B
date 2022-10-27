from django.urls import path
from .views import UserJoinApiView

urlpatterns = [
    path('join/',UserJoinApiView.as_view()),
]