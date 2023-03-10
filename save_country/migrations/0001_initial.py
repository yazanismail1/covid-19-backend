# Generated by Django 4.1.4 on 2022-12-26 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Country",
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
                ("country", models.CharField(max_length=56)),
                ("cases", models.IntegerField()),
                ("deths", models.IntegerField()),
                ("recovered", models.IntegerField()),
                ("Date", models.CharField(max_length=56)),
            ],
        ),
    ]
