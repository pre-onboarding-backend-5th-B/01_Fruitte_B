from django.db import transaction
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from cart.models import CartItem, Cart
from product.models import ProductOption
from purchase.models import PurchasedList, PayMethod, DeliveryStatus
from purchase.serializers import PurchasedListSerializer, PayMethodSerializer, DeliveryStatusSerializer


# Create your views here.
class PayMethodViewSet(ModelViewSet):
    serializer_class = PayMethodSerializer
    queryset = PayMethod.objects.all()

    def get_permissions(self):
        self.permission_classes = [IsAdminUser]
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]

        return super(PayMethodViewSet, self).get_permissions()


class DeliveryStatusViewSet(ModelViewSet):
    serializer_class = DeliveryStatusSerializer
    queryset = DeliveryStatus.objects.all()

    def get_permissions(self):
        self.permission_classes = [IsAdminUser]
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]

        return super(DeliveryStatusViewSet, self).get_permissions()


class PurchaseViewSet(ModelViewSet):
    serializer_class = PurchasedListSerializer
    queryset = PurchasedList.objects.all()
