from rest_framework import serializers

from .models import Product, ProductOption


class ProductOptionSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = ProductOption
        fields = ['id', 'product_name', 'option_detail', 'price', 'amount']


class ProductSerializer(serializers.ModelSerializer):
    options = ProductOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'thumbnail', 'options']


class ProductReadOnlySerializer(ProductSerializer):
    class Meta(ProductSerializer.Meta):
        pass


class ProductDetailOrWriteSerializer(ProductSerializer):
    class Meta(ProductSerializer.Meta):
        ProductSerializer.Meta.fields += ['detail_image', 'description']
