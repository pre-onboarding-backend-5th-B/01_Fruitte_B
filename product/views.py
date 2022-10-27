from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from product.models import Product
from product.serializers import ProductSerializer, ProductListSerializer, \
    ProductDetailSerializer, ProductWriteSerializer


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
            return ProductListSerializer
        if self.action == 'retrieve':
            return ProductDetailSerializer
        return ProductWriteSerializer

    def get_permissions(self):
        self.permission_classes = [IsAdminUser]
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]

        return super(ProductViewSet, self).get_permissions()
