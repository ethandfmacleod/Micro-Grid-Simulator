# Generated by Django 5.1.4 on 2024-12-20 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0007_rename_type_propertyinfo_display_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='propertyinfo',
            options={'ordering': ['pk']},
        ),
        migrations.AddField(
            model_name='node',
            name='isOpen',
            field=models.BooleanField(default=False),
        ),
    ]