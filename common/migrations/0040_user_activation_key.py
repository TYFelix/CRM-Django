# Generated by Django 3.2 on 2022-08-19 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0039_auto_20220202_2023"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="activation_key",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]