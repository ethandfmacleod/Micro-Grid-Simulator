# Generated by Django 5.1.4 on 2024-12-17 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0005_node_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='name',
        ),
    ]
