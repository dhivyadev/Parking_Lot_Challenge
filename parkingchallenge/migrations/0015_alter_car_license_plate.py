# Generated by Django 4.2.4 on 2023-11-09 07:09

from django.db import migrations
from django.db import models
import parkingchallenge.models


class Migration(migrations.Migration):

    dependencies = [
        ('parkingchallenge', '0014_alter_car_license_plate'),
    ]

    migrations.AlterField(
        model_name='car',
        name='license_plate',
        field=models.CharField(max_length=7, unique=True),  # Modify this line
    ),

