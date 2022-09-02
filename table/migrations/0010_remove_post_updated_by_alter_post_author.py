# Generated by Django 4.1 on 2022-09-02 18:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("table", "0009_post_updated_by_alter_post_author"),
    ]

    operations = [
        migrations.RemoveField(model_name="post", name="updated_by",),
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
