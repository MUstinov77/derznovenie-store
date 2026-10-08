from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_active', 'order')
    list_editable = ('price', 'is_active', 'order')
    list_filter = ('is_active', 'category')
    search_fields = ('name', 'description')
