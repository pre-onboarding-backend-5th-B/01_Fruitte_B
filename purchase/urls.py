from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('', views.PurchaseViewSet)
router.register('delivery', views.DeliveryStatusViewSet)
router.register('pay-method', views.PayMethodViewSet)

urlpatterns = [
    path('', include(router.urls), name='purchase')
]
