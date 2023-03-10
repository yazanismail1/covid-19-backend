# Generated by Django 4.1.4 on 2022-12-26 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("save_country", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="country",
            old_name="country",
            new_name="Country",
        ),
        migrations.RenameField(
            model_name="country",
            old_name="cases",
            new_name="TotalConfirmed",
        ),
        migrations.RenameField(
            model_name="country",
            old_name="deths",
            new_name="TotalDeaths",
        ),
        migrations.RenameField(
            model_name="country",
            old_name="recovered",
            new_name="TotalRecovered",
        ),
        migrations.AlterField(
            model_name="country",
            name="Date",
            field=models.TextField(max_length=56),
        ),
    ]
