from rest_framework import serializers

from .models import Product, ProductOption


class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOption
        read_only_fields = ('id', 'product',)
        fields = ['option_detail', 'price', 'amount']


class ProductSerializer(serializers.ModelSerializer):
    options = ProductOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductListSerializer(ProductSerializer):
    class Meta(ProductSerializer.Meta):
        fields = ['name', 'description', 'thumbnail']


class ProductDetailSerializer(ProductSerializer):
    class Meta(ProductSerializer.Meta):
        fields = ['name', 'description', 'thumbnail', 'detail_image', 'description']


class ProductWriteSerializer(serializers.ModelSerializer):
    class Meta(ProductSerializer.Meta):
        fields = ['name', 'description', 'thumbnail', 'detail_image']
