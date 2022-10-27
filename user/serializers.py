# DRF
from rest_framework import serializers
# local apps
from .models import User

class UserSerializer(serializers.ModelSerializer):    

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'join_date', 'profile_img']
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user