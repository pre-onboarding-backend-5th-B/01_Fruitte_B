from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from purchase.models import PurchasedList, PayMethod, DeliveryStatus
from purchase.serializers import PurchasedListSerializer, PayMethodSerializer, DeliveryStatusSerializer


# Create your views here.
class PayMethodViewSet(ModelViewSet):
    serializer_class = PayMethodSerializer
    queryset = PayMethod.objects.all()


class DeliveryStatusViewSet(ModelViewSet):
    serializer_class = DeliveryStatusSerializer
    queryset = DeliveryStatus.objects.all()


class PurchaseViewSet(ModelViewSet):
    serializer_class = PurchasedListSerializer
    queryset = PurchasedList.objects.all().order_by('product__name')
