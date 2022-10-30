from django.contrib.auth import authenticate, login, logout

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer


class UserJoinApiView(APIView):
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({"message": "가입 완료!"}, status=status.HTTP_200_OK)

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginApiView(APIView):
    def post(self, request):
        username = request.data.get("username", "")
        password = request.data.get("password", "")

        user = authenticate(request, username=username, password=password)

        if not user:
            return Response({"error": "아이디 혹은 비밀번호가 일치하지 않습니다."})

        login(request, user)
        return Response({"message": "성공적으로 로그인되었습니다."}, status=status.HTTP_200_OK)


class UserLogoutApiView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "성공적으로 로그아웃되었습니다."}, status=status.HTTP_200_OK)


class UserApiView(APIView):
    def get(self, request):
        return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)

    def put(self, request):
        user_serializer = UserSerializer(request.user, data=request.data, partial=True)

        if user_serializer.is_valid():
            user_serializer.save()
            return Response({"message": "성공적으로 회원정보를 수정하였습니다."}, status=status.HTTP_200_OK)

        return Response(user_serializer.error, status=status.HTTP_400_BAD_REQUEST)
