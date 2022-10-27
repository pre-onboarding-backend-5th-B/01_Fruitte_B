from rest_framework import viewsets, permissions

from product.models import Product
from product.serializers import ProductSerializer


# Create your views here.
class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    지원자 view
    """
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
