from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Cart, CartItem
from product.models import Product, ProductOption

from .serializers import CartSerializer, CartItemSerializer


class CartApiView(APIView):
    def get(self, request):
        pass

class CartItemAddApiView(APIView):
    def post(self, request, product_id, option_id):
        """
        카트 담기 기능
        URI
        /product/<int:product_id>/cart/<int:option_id/>
        {
            "quantity": 1
            }
        """
        product = Product.objects.get(id=product_id)
        option = ProductOption.objects.get(id=option_id)

        if option.product.id == product.id:
            try:
                cart = Cart.objects.get(user=request.user)
            except Cart.DoesNotExist:
                cart = Cart.objects.create(user=request.user)
                cart.save()
            try:
                cart_item = CartItem.objects.get(option=option.id, cart_id=cart.id)
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
                request.data["option"] = option.id
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
        else:
            return Response(
                {"message": "해당상품에 없는 옵션입니다."}, status=status.HTTP_400_BAD_REQUEST
            )
