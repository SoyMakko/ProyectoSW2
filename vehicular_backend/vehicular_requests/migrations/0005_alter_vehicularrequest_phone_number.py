# Generated by Django 5.1.3 on 2024-11-30 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicular_requests', '0004_vehicularrequest_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicularrequest',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
