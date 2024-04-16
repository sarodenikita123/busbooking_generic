from django.db import models


class BusBooking(models.Model):
    gen = [("WOMEN", "women"), ("MEN", "men"), ("BOY", "boy"), ("GIRL", "girl")]
    candidate_name = models.CharField(max_length=20)
    mobile_no = models.IntegerField()
    gender = models.CharField(max_length=20, choices=gen)
    place = models.CharField(max_length=20)
    bus_no = models.CharField(max_length=10)
