from django.contrib import admin

from crypto_portfolio.products.model_category import Category
from crypto_portfolio.products.model_products import Products


@admin.register(Products)
class CoinAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'slug',)
    list_filter = ('price', 'name', 'category',)
    ordering = ('name',)
    search_fields = ('name', 'product_user',)
    readonly_fields = ('slug',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
