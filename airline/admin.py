from django.contrib import admin

from .models import Travelling, Booking


class TravellingAdmin(admin.ModelAdmin):
    list_display = (
        "flight",
        "from_place",
        "to_place",
        "departure_time",
        "arrival_time",
        "total_seat",
        "available_seat",
        "ticket_rate",
        "total_collected",
    )


class BookingAdmin(admin.ModelAdmin):
    list_display = ("booked","ticket_id", "date", "no_of_seats", "Travelling", "cost",)


admin.site.register(Booking, BookingAdmin)
admin.site.register(Travelling, TravellingAdmin)
