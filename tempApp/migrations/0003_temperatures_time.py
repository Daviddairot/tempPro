# Generated by Django 5.1.3 on 2024-11-22 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tempApp', '0002_temperatures_humidity1_temperatures_humidity2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='temperatures',
            name='time',
            field=models.TimeField(default="00:00:00"),
        ),
    ]
