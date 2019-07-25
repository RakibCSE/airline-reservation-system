from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from airline.models import Booking


class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    fullname = models.CharField(max_length=60)
    email = models.EmailField(max_length=100, unique=True)
    age = models.IntegerField(null=True)


class BookingBy(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    booked = models.ForeignKey(Booking, on_delete=models.CASCADE)
