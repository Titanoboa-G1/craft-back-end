from unicodedata import category
from urllib import request

from django.views.generic import View
from django.shortcuts import get_object_or_404, render
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response

from .models import Category, Product, Order, Cart, User
from .serializers import CartSerializer, CategorySerializer, ProductSerializer
from .helpers import CartHelper

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


# class CheckoutView(View):
#     def get(self, *args, **kwargs):
#         try:
#             order = Order.object.get(user=self.request.user, order=False)
#             form = CheckOutForm()
#             context = {
#                 'form': form.
#                 'order': order
#             }
#             return Response(self.request, context)
#         except ObjectDoesNotExist:
#             message = info(self.request, "You do not have an active order")
#             return redirect()

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all().order_by('id')
    serializer_class = CartSerializer

    @action (methods=['get'], detail=False, url_path='checkout/(?P<userId>[^/.]+)', url_name='checkout')
    def checkout(self, request, *args, **kwargs):

        try:
            user = User.objects.get(pk=int(kwargs.get('userId')))
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'Error': str(e)})

        cart_helper = CartHelper(user)
        checkout_details = cart_helper.prepare_cart_for_checkout()

        if not checkout_details:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={'error': 'Cart of user is empty.'})

        return Response(status=status.HTTP_200_OK, data={'checkout_details': checkout_details})