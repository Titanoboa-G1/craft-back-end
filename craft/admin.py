from django.contrib import admin

from .models import Category, Product

# admin.site.register(Category)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    # prepopulated_fields = {'slug': ('name,')}
    # prepopulated_fields: 'slug'[str, 'name,'[str]]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "stock", "in_stock", "created"]
    list_filter = ["in_stock", "is_active"]
    list_editable = ["price", "in_stock"]
    # prepopulated_fields = {'slug': ('title',)}
