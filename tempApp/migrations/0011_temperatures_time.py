# Generated by Django 5.1.3 on 2024-11-22 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tempApp', '0010_remove_temperatures_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='temperatures',
            name='time',
            field=models.TimeField(default='00:00:00'),
        ),
    ]
