from django.contrib import admin

from .models import Travelling, Booking


admin.site.register(Booking)
admin.site.register(Travelling)
