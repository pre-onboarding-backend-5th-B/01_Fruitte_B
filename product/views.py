from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from product.models import Product, ProductOption
from product.serializers import ProductSerializer, ProductReadOnlySerializer, ProductDetailOrWriteSerializer, \
    ProductOptionSerializer


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    """
    상품을 등록, 수정, 조회, 삭제를 할 수 있음
    이때, 권한에 따라 조회만 할 수도 있고, CRUD 를 할 수 있음.
    """
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductReadOnlySerializer
        return ProductDetailOrWriteSerializer

    def get_permissions(self):
        self.permission_classes = [IsAdminUser]
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]

        return super(ProductViewSet, self).get_permissions()


class ProductOptionViewSet(viewsets.ModelViewSet):
    """
    상품 가격을 등록, 수정, 조회, 삭제를 할 수 있음
    이때, 권한에 따라 조회만 할 수도 있고, CRUD 를 할 수 있음.
    """
    queryset = ProductOption.objects.all().order_by('product_id')
    serializer_class = ProductOptionSerializer

    def perform_create(self, serializer):
        product = get_object_or_404(Product, pk=self.kwargs['product_id'])
        serializer.save(product=product)
        return super().perform_create(serializer)

    def get_queryset(self):
        return ProductOption.objects.filter(product_id=self.kwargs['product_id'])

    def get_permissions(self):
        self.permission_classes = [IsAdminUser]
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]

        return super(ProductOptionViewSet, self).get_permissions()
