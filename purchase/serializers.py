from rest_framework import serializers

from purchase.models import PayMethod, DeliveryStatus, PurchasedList


class PayMethodSerializer(serializers.ModelSerializer):
    """
    결제 종류
    - 카드
    - 현금
    """
    class Meta:
        model = PayMethod
        fields = ['pay_method']


class DeliveryStatusSerializer(serializers.ModelSerializer):
    """
    배송 수단
    - 택배
    - 직접
    """

    class Meta:
        model = DeliveryStatus
        fields = ['delivery_status']


class PurchasedListSerializer(serializers.ModelSerializer):
    """
    결제 수단
    """

    class Meta:
        model = PurchasedList
        fields = ['pay_method', 'delivery_status', 'purchased_at', 'is_present']
