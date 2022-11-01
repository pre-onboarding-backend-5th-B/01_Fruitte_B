from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    """
    Product - 상품
    """
    name = models.CharField(max_length=100,
                            help_text='상품명을 입력해주세요.')
    thumbnail = models.ImageField(upload_to="static/product/thumbnail_img",
                                  blank=True,
                                  help_text='썸네일을 ')
    detail_image = models.ImageField(upload_to="static/product/detail_img", blank=True)
    description = models.TextField(help_text='상품에 대한 설명을 입력하세요.')
    register_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False, help_text='공개 설정')

    def __str__(self):
        return self.name


class ProductOption(models.Model):
    """
    Product 필수 옵션
    """
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    option_detail = models.CharField(max_length=50,
                                     help_text='상품에 대한 수량 혹은 무게에 대한 설명을 입력하세요.')
    price = models.IntegerField(help_text='가격을 입력하세요.')
    amount = models.IntegerField(blank=True,
                                 validators=[MinValueValidator(0)],
                                 help_text='재고량을 입력하세요.')

    def __str__(self):
        return f'{self.product.name} - {self.option_detail}1'
