import datetime

from django.db import models

from crypto_portfolio.accounts.models import AppUser
from crypto_portfolio.products.model_category import Category
from crypto_portfolio.products.model_products import Products


class Order(models.Model):

    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
    )

    customer = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
    )

    quantity = models.IntegerField(
        default=1,
        db_column='order_quantity',
    )

    date = models.DateField(
        default=datetime.datetime.today,
    )

    status = models.BooleanField(
        default=False,
    )

    transaction_id = models.CharField(
        max_length=200,
        null=True,
    )

    def place_order(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')


class OrderCrypto(models.Model):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class UserPortfolio(models.Model):
    str_fields = ('id', 'coin_name')
    MAX_NAME = 30

    crypto_name = models.CharField(
        max_length=MAX_NAME,
        null=True,
        blank=True,
    )

    crypto_photo = models.URLField(
        null=True,
        blank=True,
    )

    slug = models.SlugField(
        null=True,
        blank=True,
    )

    crypto_price = models.FloatField(
        null=True,
        blank=True,
    )

    crypto_market_cap = models.FloatField(
        null=True,
        blank=True,
    )

    crypto_volume = models.FloatField(
        null=True,
        blank=True,
    )

    quantity = models.FloatField(
        null=True,
        blank=True,
    )

    crypto_user = models.IntegerField(
        null=True,
        blank=True,
    )

    crypto_product = models.IntegerField(
        null=True,
        blank=True,
    )

    @staticmethod
    def get_products_by_user(ids):
        return UserPortfolio.objects.filter(crypto_user=ids)
