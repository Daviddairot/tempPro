# Generated by Django 5.1.3 on 2024-11-22 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tempApp', '0006_alter_temperatures_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperatures',
            name='time',
            field=models.TimeField(default=1),
            preserve_default=False,
        ),
    ]