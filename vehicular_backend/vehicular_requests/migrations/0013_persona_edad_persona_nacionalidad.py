# Generated by Django 5.1.3 on 2024-12-01 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicular_requests', '0012_rename_serial_number_vehiculo_numero_serie_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='edad',
            field=models.IntegerField(default=44),
        ),
        migrations.AddField(
            model_name='persona',
            name='nacionalidad',
            field=models.CharField(default='Mexicana', max_length=50),
        ),
    ]
