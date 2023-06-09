# Generated by Django 3.2.16 on 2022-12-19 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20221218_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userportfolio',
            name='crypto_market_cap',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userportfolio',
            name='crypto_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='userportfolio',
            name='crypto_photo',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userportfolio',
            name='crypto_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userportfolio',
            name='crypto_volume',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userportfolio',
            name='quantity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userportfolio',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
