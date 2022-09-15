from django.urls import path

from .views import (
    CategoryListCreateView,
    ProductDetailView,
    ProductListCreateView,
)

app_name = "craft"

urlpatterns = [
    path("", ProductListCreateView.as_view(), name="product_list"),
    path("<slug:slug>", CategoryListCreateView.as_view(), name="category_list"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
]
