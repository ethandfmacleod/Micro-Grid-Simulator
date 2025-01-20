# Generated by Django 5.1.4 on 2025-01-05 06:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowsheet', '0010_remove_weatherdata_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controller',
            name='weather',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='weather_controller', to='flowsheet.weatherdata'),
        ),
    ]