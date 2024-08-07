# Generated by Django 5.0.6 on 2024-07-07 18:18

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Food_POS", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ingredient",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("3a0f1906-9683-4468-bfb8-a69ec57cb9e7"),
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("69e84492-54f9-4b43-95b0-75cd2fa6dba8"),
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("e396cec4-2de3-465c-88cf-9d92e4eeb6e1"),
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
