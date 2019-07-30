from django.conf import settings
from django.db import models

from django.utils import timezone

import datetime

class Travelling(models.Model):
    IMAGE_URL = "https://media.apnarm.net.au/media/images/2018/01/05/" \
                "imagev172581b44162efca316c368ceb9332a48-de5o2q14aokk572qjp2_ct1880x930.jpg"

    flight = models.CharField(max_length=60)
    flight_image = models.URLField(max_length=200, default=IMAGE_URL)
    from_place = models.CharField(max_length=20)
    to_place = models.CharField(max_length=20)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    total_seat = models.IntegerField()
    available_seat = models.IntegerField()
    ticket_rate = models.IntegerField()
    total_collected = models.IntegerField(default=0)

    def __str__(self):
        return self.flight + " From " + self.from_place + " To " + self.to_place


class Booking(models.Model):
    booked = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ticket_id = models.CharField(null=False, max_length=20)
    date = models.CharField(null=False, max_length=30)
    no_of_seats = models.IntegerField()
    Travelling = models.ForeignKey(Travelling, on_delete=models.CASCADE)
    cost = models.IntegerField(default=0)
