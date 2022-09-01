# Generated by Django 4.1 on 2022-09-01 19:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("table", "0005_alter_post_add_alter_post_neg_alter_post_square"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="year",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1900),
                    django.core.validators.MaxValueValidator(2022),
                ],
                verbose_name="year",
            ),
        ),
    ]
