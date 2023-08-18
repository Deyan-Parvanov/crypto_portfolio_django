from django.contrib.auth import models as auth_models
from django.core import validators, exceptions
from django.db import models


def names_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise exceptions.ValidationError("The name must contain only letters!")


class AppUser(auth_models.AbstractUser):
    MIN_LEN_FIRST_NAME = 2
    MIN_LEN_LAST_NAME = 2
    MIN_AGE = 18

    first_name = models.CharField(
        max_length=30,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            names_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=30,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            names_only_letters,
        )
    )

    email = models.EmailField(
        unique=True,
    )

    age = models.IntegerField(
        validators=(
            validators.MinValueValidator(MIN_AGE),
        ),
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )
