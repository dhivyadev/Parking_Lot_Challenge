# Generated by Django 4.2.4 on 2023-11-08 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkingchallenge', '0002_parkinglot_allocated_spots_parkinglot_num_spots_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parkinglot',
            name='allocated_spots',
        ),
        migrations.RemoveField(
            model_name='parkinglot',
            name='num_spots',
        ),
        migrations.RemoveField(
            model_name='parkinglot',
            name='spot_size_length',
        ),
        migrations.RemoveField(
            model_name='parkinglot',
            name='spot_size_width',
        ),
        migrations.AddField(
            model_name='parkinglot',
            name='is_full',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='parkinglot',
            name='spot_size',
            field=models.CharField(default='8x12', max_length=10),
        ),
        migrations.DeleteModel(
            name='ParkingSlot',
        ),
    ]