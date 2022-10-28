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
        read_only_fields = ['id']
        fields = ['name', 'description', 'thumbnail', 'options']


class ProductReadOnlySerializer(ProductSerializer):
    class Meta(ProductSerializer.Meta):
        pass


class ProductDetailOrWriteSerializer(ProductSerializer):
    class Meta(ProductSerializer.Meta):
        ProductSerializer.Meta.fields += ['detail_image', 'description']
