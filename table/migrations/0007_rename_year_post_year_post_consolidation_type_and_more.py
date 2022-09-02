# Generated by Django 4.1 on 2022-09-02 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("table", "0006_post_year"),
    ]

    operations = [
        migrations.RenameField(model_name="post", old_name="year", new_name="Year",),
        migrations.AddField(
            model_name="post",
            name="Consolidation_Type",
            field=models.CharField(
                blank=True,
                choices=[("Daily", "Daily"), ("Monthly", "Monthly")],
                max_length=100,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="File_Type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Inventory", "Inventory"),
                    ("Distributory Sales", "Distributory Sales"),
                ],
                max_length=100,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="Month",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (1, "Jan"),
                    (2, "Feb"),
                    (3, "Mar"),
                    (4, "Apr"),
                    (5, "May"),
                    (6, "Jun"),
                    (7, "Jul"),
                    (8, "Aug"),
                    (9, "Sept"),
                    (10, "Oct"),
                    (11, "Nov"),
                    (12, "Dec"),
                ],
                null=True,
            ),
        ),
    ]