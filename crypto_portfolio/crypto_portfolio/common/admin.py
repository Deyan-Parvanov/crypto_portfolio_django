from django.contrib import admin

from crypto_portfolio.common.models import Order, OrderCrypto, UserPortfolio


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderCrypto)
class OrderCryptoAdmin(admin.ModelAdmin):
    pass


@admin.register(UserPortfolio)
class UserPortfolioAdmin(admin.ModelAdmin):
    ordering = ('crypto_name',)
    search_fields = ('crypto_name',)

