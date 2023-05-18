# import datetime
#
# from django.db import models
#
# from crypto_portfolio.accounts.models import AppUser
# from crypto_portfolio.products-test.model_product import Products
#
#
# class Order(models.Model):
#     ADDRESS_LEN = 50
#     PHONE_LEN = 50
#
#     product = models.ForeignKey(
#         Products,
#         on_delete=models.CASCADE,
#     )
#
#     user = models.ForeignKey(
#         AppUser,
#         on_delete=models.CASCADE,
#     )
#
#     quantity = models.IntegerField(
#         default=1,
#     )
#
#     price = models.IntegerField()
#
#     date = models.DateField(
#         default=datetime.datetime.today,
#     )
#
#     status = models.BooleanField(
#         default=False,
#     )
#
#     def place_order(self):
#         self.save()
#
#     @staticmethod
#     def get_orders_by_customer(customer_id):
#         return Order.objects.filter(customer=customer_id).order_by('-date')
