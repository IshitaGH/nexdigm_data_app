# Generated by Django 4.1.1 on 2022-09-08 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("table", "0011_alter_post_add_alter_post_author_alter_post_neg_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Data",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Distributor", models.IntegerField()),
                (
                    "Region",
                    models.CharField(
                        blank=True,
                        choices=[("A", "a"), ("B", "b")],
                        max_length=100,
                        null=True,
                    ),
                ),
                ("Name", models.CharField(blank=True, max_length=100, null=True)),
                ("Selection", models.BooleanField(blank=True, null=True)),
            ],
        ),
    ]