# Generated by Django 4.2.7 on 2023-12-19 22:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("test_app", "0002_simplemodel_numeric_simplemodel_truthy"),
    ]

    operations = [
        migrations.AlterField(
            model_name="relatedmodel",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]