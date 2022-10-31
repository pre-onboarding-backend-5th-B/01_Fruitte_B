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
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # 본인 것만 봐야함
        return PurchasedList.objects.select_related('cart').filter(
            cart__user=self.request.user
        )

    # 구매 내역의 create 는 결제 하기 기능과 같다고 생각
    def perform_create(self, serializer):
        with transaction.atomic():
            cart = Cart.objects.get(pk=serializer.validated_data.get('cart').id)
            if not self.request.user == cart.user:
                raise ValidationError('결제는 장바구니를 담은 사용자와 일치해야 합니다.')
            cart_items = CartItem.objects.select_related('option').filter(
                cart=cart
            ).order_by('product_id')  # cart_item 에 담긴 부분을 확인함
            product_details = ProductOption.objects.filter(
                id__in=[x.option.id for x in cart_items]  # cart_item 에 담긴 product detail 을 확인, 재고 수량을 줄임
            ).order_by('product_id')

            assert len(cart_items) == len(product_details)
            for cart_item, product_detail in zip(cart_items, product_details):
                product_detail.amount -= cart_item.quantity
                if product_detail.amount < 0:
                    raise ValidationError(f'재고가 부족합니다. '
                                          f'현재 {product_detail.product.name}은/는 {product_detail.amount}개 남았습니다.')
                product_detail.save()

            purchase = serializer.save(cart=cart, user=self.request.user)
            return purchase
