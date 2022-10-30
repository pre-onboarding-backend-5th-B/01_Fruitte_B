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

    class Meta:
        model = PurchasedList
        fields = '__all__'
