from django.contrib import admin

from crypto_portfolio.products.model_category import Category
from crypto_portfolio.products.model_products import Products


@admin.register(Products)
class CoinAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
