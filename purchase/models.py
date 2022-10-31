from django.db import models

from cart.models import Cart
from product.models import Product, ProductOption
from user.models import User


class PayMethod(models.Model):
    """
    결제 수단
    """
    pay_method = models.CharField(max_length=20)

    def __str__(self):
        return self.pay_method


class DeliveryStatus(models.Model):
    """
    배송 수단
    """
    delivery_status = models.CharField(max_length=10)

    def __str__(self):
        return self.delivery_status


class PurchasedList(models.Model):
    """
    결제 하기
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)  # cart 당 하나의 구매 내역만 있어야 함
    pay_method = models.ForeignKey("PayMethod", on_delete=models.CASCADE)  # cart_item 에 정보가 있음
    delivery_status = models.ForeignKey("DeliveryStatus", on_delete=models.CASCADE)
    purchased_at = models.DateTimeField(auto_now_add=True)
    is_present = models.BooleanField(default=True)

    def __str__(self):
        product_option = self.cart.cartitem_set.product_option
        return f'{self.cart.cartitem_set.product.name}' \
               f'({product_option.option_detail}' \
               f'{product_option.price} - {product_option.amount})'
