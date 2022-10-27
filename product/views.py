from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from product.models import Product
from product.serializers import ProductSerializer, ProductListSerializer, \
    ProductDetailSerializer, ProductWriteSerializer


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    """
    지원자 view
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
