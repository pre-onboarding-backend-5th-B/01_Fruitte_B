from django.db import models
from user.models import User
from product.models import Product


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
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    pay_method = models.ForeignKey("PayMethod", on_delete=models.CASCADE)
    delivery_status = models.ForeignKey("DeliveryStatus", on_delete=models.CASCADE)
    purchased_at = models.DateTimeField(auto_now_add=True)
    is_present = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.product.cart_set.name}({self.product.cart_set.price})'
