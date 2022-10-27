from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
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
