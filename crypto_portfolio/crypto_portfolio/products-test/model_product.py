# from django.core import validators
# from django.db import models
#
# from crypto_portfolio.products.model_category import Category
#
#
# class Products(models.Model):
#     str_fields = ('id', 'coin_name')
#     MAX_NAME = 30
#     MIN_PRICE = 0
#     DESCRIPTION_LEN = 200
#
#     name = models.CharField(
#         max_length=MAX_NAME,
#         null=False,
#         blank=False,
#     )
#
#     photo = models.URLField(
#         null=False,
#         blank=False,
#     )
#
#     slug = models.SlugField(
#         unique=True,
#         null=False,
#         blank=True,
#     )
#
#     price = models.FloatField(
#         validators=[
#             validators.MinValueValidator(MIN_PRICE),
#         ],
#         null=False,
#         blank=False,
#     )
#
#     description = models.CharField(
#         max_length=DESCRIPTION_LEN,
#         default='',
#         null=True,
#         blank=True,
#     )
#
#     category = models.ForeignKey(
#         Category,
#         on_delete=models.CASCADE,
#         default=1
#     )
#
#     @staticmethod
#     def get_products():
#         return Products.objects.all()
#
#     @staticmethod
#     def get_products_by_id(ids):
#         return Products.objects.filter(id__in=ids)
#
#     @staticmethod
#     def get_products_by_category_id(category_id):
#         if category_id:
#             return Products.objects.filter(category=category_id)
#         else:
#             return Products.get_products()
