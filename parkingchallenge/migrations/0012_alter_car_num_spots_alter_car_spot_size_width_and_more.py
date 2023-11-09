# Generated by Django 4.2.4 on 2023-11-09 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkingchallenge', '0011_car_spot_size_length_car_spot_size_width_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='num_spots',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='spot_size_width',
            field=models.IntegerField(default='12', max_length=10),
        ),
        migrations.AlterField(
            model_name='parkinglot',
            name='num_spots',
            field=models.IntegerField(default=0),
        ),
    ]
