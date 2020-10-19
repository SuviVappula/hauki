# Generated by Django 3.1.2 on 2020-10-19 06:11

import enumfields.fields
from django.db import migrations

import hours.enums


class Migration(migrations.Migration):

    dependencies = [
        ("hours", "0002_add_organization_to_resource"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalopeninghours",
            name="period_type",
            field=enumfields.fields.EnumField(
                default="undefined",
                enum=hours.enums.PeriodType,
                max_length=100,
                verbose_name="Period type",
            ),
        ),
        migrations.AddField(
            model_name="openinghours",
            name="period_type",
            field=enumfields.fields.EnumField(
                default="undefined",
                enum=hours.enums.PeriodType,
                max_length=100,
                verbose_name="Period type",
            ),
        ),
    ]
