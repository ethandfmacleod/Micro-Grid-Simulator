# Generated by Django 5.1.4 on 2025-01-04 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flowsheet', '0005_rename_irradiance_dhi_weatherdata_irradiance_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weatherdata',
            name='date',
        ),
    ]