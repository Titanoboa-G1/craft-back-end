from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Cart, Category, Product, User

# from accounts.serializers import UserSerializer


class ProductSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = "__all__"

    def get_user(self, obj):
        return obj.user.all().values()

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