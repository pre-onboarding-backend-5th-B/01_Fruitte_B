from django.db import models
from user.models import User
from product.models import Product, ProductOption


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    option = models.ForeignKey(ProductOption, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    is_present = models.BooleanField(default=True)
