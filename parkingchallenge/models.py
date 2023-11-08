from django.db import models


class Car(models.Model):
    license_plate = models.CharField(max_length=7, unique=True)  # Unique license plate
    num_spots = models.IntegerField(null=True, blank=True)  # Slot number assigned to the car
    square_footage = models.IntegerField(max_length=20, default="2000")
    spot_size_width = models.IntegerField(max_length=10, default="12")
    spot_size_length = models.IntegerField(max_length=10, default="8")
class ParkingLot(models.Model):
    square_footage = models.IntegerField(default=2000)
    spot_size_width = models.IntegerField(default=10)
    spot_size_length = models.IntegerField(default=12)
    num_spots = models.IntegerField(default=20)

    def save(self, *args, **kwargs):
        self.num_spots = self.square_footage // (self.spot_size_width * self.spot_size_length)
        super(ParkingLot, self).save(*args, **kwargs)



