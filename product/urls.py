from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('', views.ProductViewSet)
# HACK: product id 에 종속 되어서 url 을 다음과 설계함
router.register(r'(?P<product_id>\d+)/option', views.ProductOptionViewSet)

urlpatterns = [
    path('', include(router.urls), name='product')
]
