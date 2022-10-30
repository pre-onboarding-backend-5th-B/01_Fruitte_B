from django.urls import path
from .views import CartApiView, CartEditApiView

urlpatterns = [
    path("", CartApiView.as_view(), name="cart"),
    path("<int:item_id>/", CartEditApiView.as_view(), name="cart_edit"),
]
