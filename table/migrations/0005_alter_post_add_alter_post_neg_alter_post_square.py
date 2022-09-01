# Generated by Django 4.1 on 2022-09-01 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("table", "0004_alter_post_add_alter_post_neg_alter_post_square"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="add",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="neg",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="square",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
    ]