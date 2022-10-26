from django.db import models
from user.models import User
from product.models import Product


class PayMethod(models.Model):
    pay_method = models.CharField(max_length=20)


class DeliveryStatus(models.Model):
    delivery_status = models.CharField(max_length=10)


class PurchasedList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    pay_method = models.ForeignKey("PayMethod", on_delete=models.CASCADE)
    delivery_status = models.ForeignKey("DeliveryStatus", on_delete=models.CASCADE)
    purchased_at = models.DateTimeField(auto_now_add=True)
    is_present = models.BooleanField(default=True)
