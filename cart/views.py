from urllib import response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Cart, CartItem
from product.models import Product, ProductOption
from product.serializers import ProductOptionSerializer
from .serializers import CartSerializer, CartItemSerializer


class CartApiView(APIView):
    def get(self, request):
        # 카트 아이템 리스트
        cart = Cart.objects.get(user=request.user)
        item_query_set = CartItem.objects.filter(cart_id=cart.id)
        return Response(
            CartItemSerializer(item_query_set, many=True).data,
            status=status.HTTP_200_OK,
        )


class CartEditApiView(APIView):
    def get(self, request, item_id):
        cart_item = get_object_or_404(CartItem, id=item_id)
        product_option = ProductOption.objects.filter(
            product=cart_item.option.product.id
        )
        product_option_list = [
            dict(x) for x in ProductOptionSerializer(product_option, many=True).data
        ]

        serializer = CartItemSerializer(cart_item).data
        serializer["option available"] = product_option_list

        return Response(serializer, status=status.HTTP_200_OK)

    def put(self, request, item_id):
        # 필수 기능 : 옵션 변경, 수량 변경
        cart_item = get_object_or_404(CartItem, id=item_id)

        serializer = CartItemSerializer(cart_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, sataus=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, item_id):
        cart_item = get_object_or_404(CartItem, id=item_id)
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
                request.data["cart"] = cart.id
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
