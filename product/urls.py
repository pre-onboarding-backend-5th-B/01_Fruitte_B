from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('', views.ProductViewSet)

urlpatterns = [
    # path('', views.index, name='index'),
    path('', include(router.urls), name='recruit')
]
