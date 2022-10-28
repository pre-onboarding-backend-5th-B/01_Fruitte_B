from django.urls import path
from .views import CartApiView, CartItemApiView

urlpatterns = [
    path("", CartApiView.as_view(), name="cart"),
]
