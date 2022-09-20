from django.urls import path, include
from rest_framework import routers

from .views import (
    CategoryListCreateView,
    ProductDetailView,
    ProductListCreateView,
    CartListCreateView,
    # CartViewSet,
)

app_name = "craft"

# router = routers.DefaultRouter()
# router.register(r'cart', CartViewSet)

# router.register('cart', CartViewSet, basename='cart')   

urlpatterns = [
    # path('', include((router.urls, 'cart'))),
    path("", ProductListCreateView.as_view(), name="product_list"),
    path("<slug:slug>", CategoryListCreateView.as_view(), name="category_list"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("cart/", CartListCreateView.as_view(), name="cart"),
    # path("cart/", include((router.urls, 'craft.cart'))),
    ]

# ]+router.urls
