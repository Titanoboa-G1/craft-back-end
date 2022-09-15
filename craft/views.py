from unicodedata import category
from django.shortcuts import render, get_object_or_404

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer

# Create your views here.

class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [OwnerOnly]

class CategoryListCreateView(ListCreateAPIView):
    # queryset = Category.objects.all()
    # serializer_class = CategorySerializer

    # category_id = Category.slug
    # print(11111111111111111111111,category_id)
    
    # queryset = Product.objects.filter(category='category')
    serializer_class = CategorySerializer



    def get(self, request, slug=None):
        category = get_object_or_404(Category, slug=slug)
        print(2222222222,category)
        products = Product.objects.filter(category=category).values()
        print(1111111111111,products)
        return Response(products, status=status.HTTP_200_OK)

