from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer

class UserJoinApiView(APIView):
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({"message":"가입 완료!"}, status=status.HTTP_200_OK)
        
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)