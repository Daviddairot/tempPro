# Generated by Django 5.1.3 on 2024-11-22 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tempApp', '0007_alter_temperatures_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='temperatures',
            name='time',
        ),
    ]
