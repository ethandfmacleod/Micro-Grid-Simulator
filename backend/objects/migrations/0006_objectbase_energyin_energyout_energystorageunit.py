# Generated by Django 5.1.4 on 2024-12-09 05:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0005_delete_energyin'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='objects', to='objects.project')),
            ],
        ),
        migrations.CreateModel(
            name='EnergyIn',
            fields=[
                ('objectbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='objects.objectbase')),
                ('watts', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0.0)),
                ('daily_emissions', models.IntegerField(default=0)),
                ('type', models.CharField(choices=[('default', 'Default'), ('solar_panel', 'Solarpanel'), ('wind_turbine', 'Windturbine')], default='default')),
            ],
            bases=('objects.objectbase',),
        ),
        migrations.CreateModel(
            name='EnergyOut',
            fields=[
                ('objectbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='objects.objectbase')),
                ('watts', models.IntegerField(default=0)),
                ('daily_emissions', models.IntegerField(default=0)),
                ('type', models.CharField(choices=[('default', 'Default'), ('factory_model', 'Factorymodel'), ('complex_home', 'Complexhome'), ('general_consumer', 'Generalconsumer')], default='default')),
            ],
            bases=('objects.objectbase',),
        ),
        migrations.CreateModel(
            name='EnergyStorageUnit',
            fields=[
                ('objectbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='objects.objectbase')),
                ('capacity', models.FloatField(default=0)),
                ('charge_level', models.FloatField(default=0)),
                ('price', models.FloatField(default=0)),
                ('type', models.CharField(choices=[('default', 'Default'), ('lithium_ion', 'Lithiumion')], default='default')),
            ],
            bases=('objects.objectbase',),
        ),
    ]