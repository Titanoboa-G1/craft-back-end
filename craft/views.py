from unicodedata import category

from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

# Create your views here.


class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [OwnerOnly]


class CategoryListCreateView(ListCreateAPIView):
    serializer_class = CategorySerializer

    def get(self, request, slug=None):
        category = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(category=category).values()
        return Response(products, status=status.HTTP_200_OK)
