from django.conf import settings
from django.db import models


class Travelling(models.Model):
	flight = models.CharField(max_length=60)
	from_place = models.CharField(max_length=20)
	to_place = models.CharField(max_length=20)
	departure_time = models.TimeField()
	arrival_time = models.TimeField()
	total_seat = models.IntegerField()
	available_seat = models.IntegerField()
	ticket_rate = models.IntegerField()
	total_collected = models.IntegerField(default=0)


class Booking(models.Model):
	booked = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	no_of_seats = models.IntegerField()
	Travelling = models.ForeignKey(Travelling, on_delete=models.CASCADE)
	cost = models.IntegerField(default=0)
