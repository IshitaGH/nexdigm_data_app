# Generated by Django 4.1 on 2022-09-02 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("table", "0010_remove_post_updated_by_alter_post_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="add",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=500, null=True
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="neg",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=500, null=True
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="square",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=500, null=True
            ),
        ),
    ]
