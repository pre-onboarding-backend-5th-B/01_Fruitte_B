from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to="static/product/thumbnail_img", blank=True)
    detail_image = models.ImageField(upload_to="static/product/detail_img", blank=True)
    description = models.TextField()
    register_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)


class ProductOption(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    option_detail = models.CharField(max_length=50)
    price = models.IntegerField()
    amount = models.IntegerField(blank=True)
