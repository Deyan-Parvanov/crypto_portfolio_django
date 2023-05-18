from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models


class AppUser(auth_models.AbstractUser):
    MIN_LEN_FIRST_NAME = 2
    MIN_LEN_LAST_NAME = 2
    MIN_AGE = 18

    first_name = models.CharField(
        max_length=30,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
        )
    )

    last_name = models.CharField(
        max_length=30,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
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

    profile_picture = models.ImageField(
        upload_to='profile_images/',
        blank=True,
        null=True,
    )
