from django.db import models


class Category(models.Model):
    MAX_LEN = 30

    name = models.CharField(
        max_length=MAX_LEN,
    )

    @staticmethod
    def get_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name
