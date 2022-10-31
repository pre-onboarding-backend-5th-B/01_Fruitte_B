from rest_framework import serializers

from cart.serializers import CartItemSerializer
from purchase.models import PayMethod, DeliveryStatus, PurchasedList


class PayMethodSerializer(serializers.ModelSerializer):
    """
    결제 종류
    - 카드
    - 현금
    """

    class Meta:
        model = PayMethod
        fields = '__all__'


class DeliveryStatusSerializer(serializers.ModelSerializer):
    """
    배송 수단
    - 택배
    - 직접
    """

    class Meta:
        model = DeliveryStatus
        fields = '__all__'


class PurchasedListSerializer(serializers.ModelSerializer):
    """
    결제 수단
    """
    cart_items_detail = serializers.SerializerMethodField()

    @staticmethod
    def get_cart_items_detail(obj):
        product_detail = obj.cart.cartitem_set.all()
        return CartItemSerializer(product_detail, many=True).data

    class Meta:
        model = PurchasedList
        fields = ['cart', 'cart_items_detail', 'pay_method', 'delivery_status', 'is_present']
