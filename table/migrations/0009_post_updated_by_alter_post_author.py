# Generated by Django 4.1 on 2022-09-02 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("table", "0008_post_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="post_update",
                to=settings.AUTH_USER_MODEL,
                verbose_name="last updated by",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="post_create",
                to=settings.AUTH_USER_MODEL,
                verbose_name="author",
            ),
        ),
    ]