# Generated by Django 5.0.6 on 2024-07-07 23:11

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("emr", "0002_leadstatus_active_alter_lead_id_alter_person_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lead",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("d7e3c8dc-62b8-41c4-8950-09b9990e5f38"),
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("2e43c443-7922-41b0-bcb4-264814fbb050"),
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
