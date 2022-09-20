from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Cart, Category, Product, User

# from accounts.serializers import UserSerializer


class ProductSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = "__all__"

    def get_created_by(self, obj):
        # return obj.created_by.all().values()
        return {
            'created_by': obj.created_by.email,
            'username': obj.created_by.username,
        }

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'created_at', 'updated_at']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'user', 'item', 'quantity', 'created_at', 'updated_at']