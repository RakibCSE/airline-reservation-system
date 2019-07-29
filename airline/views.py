import random

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, HttpResponseRedirect

from airline.models import Travelling, Booking


def home(request):
    flight_data = sorted(Travelling.objects.all().order_by('ticket_rate')[:10], key= lambda x : random.random())
    if flight_data:
        response = render(request, "airline/home.html", {
            "flight_data": flight_data[:10],
            "session": request.session
        })
        return response

    response = render(request, "airline/home.html")
    return response


def search(request):
    if request.GET:
        flight_data = ""
        get_data = request.GET

        from_place = request.session['from_place'] = get_data['from_place'].strip()
        to_place = request.session['to_place'] = get_data['to_place'].strip()
        flight_date = request.session['flight_date'] = get_data['flight_date']
        page = get_data.get("page", 1)

        if from_place and to_place:
            flight_data = Travelling.objects.filter(
                Q(from_place__icontains=from_place) & Q(to_place__icontains=to_place)
            )

        paginator = Paginator(list(flight_data), 10)
        try:
            flight_data = paginator.page(page)
        except PageNotAnInteger:
            flight_data = paginator.page(1)
        except EmptyPage:
            flight_data = paginator.page(paginator.num_pages)

        response = render(request, "airline/home.html", {
            "flight_data": flight_data,
            "session": request.session
        })
        return response

    response = render(request, "airline/home.html")
    return response


@login_required
def book(request, flight_id):
    flight_data = Travelling.objects.get(id=flight_id)
    response = render(request, "airline/book.html", {
        "flight_data": flight_data
    })
    return response


@login_required
def save_booking(request, flight_id):
    if request.POST:
        post_data = request.POST
        no_of_seats = post_data['no_of_seats']
        total_amount = post_data['total_amount']

        flight_data = Travelling.objects.get(id=flight_id)

        booking = Booking()
        booking.booked = request.user
        booking.no_of_seats = no_of_seats
        booking.cost = total_amount
        booking.Travelling = flight_data
        booking.save()

        flight_data.available_seat -= int(no_of_seats)
        flight_data.total_collected += int(total_amount)
        flight_data.save()

        response = HttpResponseRedirect("/")
        return response

    response = HttpResponseRedirect("/flight/{}/book".format(flight_id))
    return response


@login_required
def cancel_booking(request, user_id, flight_id):

    booking_data = Booking.objects.get(
        Q(booked_id=user_id) & Q(Travelling_id=flight_id)
    )

    travelling_data = Travelling.objects.get(id=flight_id)
    travelling_data.available_seat += booking_data.no_of_seats
    travelling_data.total_collected -= booking_data.cost
    travelling_data.save()

    booking_data.delete()

    response = HttpResponseRedirect("/{}/bookings".format(user_id))
    return response


@login_required
def bookings(request, user_id):
    booking_data = Booking.objects.filter(booked_id=user_id)

    response = render(request, "airline/bookings.html", {
        "booking_data": booking_data,
        "session": request.session
    })
    return response
