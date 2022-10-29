from django.urls import path, include
from rest_framework import routers

from . import views
from cart.views import CartItemAddApiView

router = routers.DefaultRouter()
router.register('', views.ProductViewSet)
# HACK: product id 에 종속 되어서 url 을 다음과 설계함
router.register(r'(?P<product_id>\d+)/option', views.ProductOptionViewSet)

urlpatterns = [
    path('<int:product_id>/option/<int:option_id>/', CartItemAddApiView.as_view(), name='add_cart'),
    path('', include(router.urls), name='product')
]
