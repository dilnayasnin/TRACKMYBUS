# Generated by Django 5.1.6 on 2025-02-18 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_driver_model_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver_model',
            name='bus_type',
        ),
    ]
