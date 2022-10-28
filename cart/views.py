from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Cart, CartItem
from product.models import Product

from .serializers import CartSerializer, CartItemSerializer


class CartApiView(APIView):
    def get(self, request):
        pass


class CartItemApiView(APIView):
    def post(self, request, pk):
        product = Product.objects.get(id=pk)

        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user=request.user)
            cart.save()
        try:
            cart_item = CartItem.objects.get(product=product.id, cart_id=cart.id)
            cart_item.quantity += request.data["quantity"]
            cart_item.save()
            return Response(
                {
                    "message": f"선택하신 상품 수량 {request.data['quantity']} 개를 추가하여 총{cart_item.quantity}개를 쇼핑카드에 담았습니다."
                },
                status=status.HTTP_201_CREATED,
            )

        except CartItem.DoesNotExist:
            request.data["cart_id"] = cart.id
            request.data["product"] = product.id
            serializer = CartItemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "message": f"선택하신 상품 수량 {request.data['quantity']} 개를 쇼핑카드에 담았습니다."
                    },
                    status=status.HTTP_201_CREATED,
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
