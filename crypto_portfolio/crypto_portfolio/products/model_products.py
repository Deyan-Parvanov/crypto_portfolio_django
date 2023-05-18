from django.core import validators
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

from crypto_portfolio.products.model_category import Category
from crypto_portfolio.core.model_mixins import StrFromFieldsMixin

UserModel = get_user_model()


class Products(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'coin_name')
    MAX_NAME = 30
    MIN_PRICE = 0
    MIN_MARKET_CAP = 0
    MIN_VOLUME = 0

    name = models.CharField(
        max_length=MAX_NAME,
        null=False,
        blank=False,
    )

    photo = models.URLField(
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    price = models.FloatField(
        validators=[
            validators.MinValueValidator(MIN_PRICE),
        ],
        null=False,
        blank=False,
    )

    market_cap = models.FloatField(
        validators=[
            validators.MinValueValidator(MIN_MARKET_CAP)
        ],
        null=False,
        blank=False,
    )

    volume = models.FloatField(
        validators=[
            validators.MinValueValidator(MIN_VOLUME)
        ],
        null=False,
        blank=False,
    )

    product_user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        default=1,
    )

    @staticmethod
    def get_products():
        return Products.objects.all()

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)

    @staticmethod
    def get_products_by_category_id(category_id):
        if category_id:
            return Products.objects.filter(category=category_id)
        else:
            return Products.get_products()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')

        return super().save(*args, **kwargs)


