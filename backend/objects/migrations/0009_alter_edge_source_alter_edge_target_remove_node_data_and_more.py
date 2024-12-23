# Generated by Django 5.1.4 on 2024-12-21 04:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0008_alter_propertyinfo_options_node_isopen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edge',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_node', to='objects.node'),
        ),
        migrations.AlterField(
            model_name='edge',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_node', to='objects.node'),
        ),
        migrations.RemoveField(
            model_name='node',
            name='data',
        ),
        migrations.AddField(
            model_name='node',
            name='calculation_mode',
            field=models.CharField(default='Default'),
        ),
        migrations.AddField(
            model_name='propertyinfo',
            name='disabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='propertyset',
            name='node',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='property_sets', to='objects.node'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='propertyset',
            name='name',
            field=models.CharField(default='Property Set', max_length=64),
        ),
        migrations.DeleteModel(
            name='ObjectBase',
        ),
    ]
