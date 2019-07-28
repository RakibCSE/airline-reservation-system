from django.urls import path, re_path

from . import views

app_name = "airline"

urlpatterns = [
    path('', views.home, name="home"),
    path('flight', views.search, name="search"),
    re_path(r'(?P<user_id>\d+)/bookings', views.bookings, name="bookings"),
    re_path(r'flight/(?P<flight_id>\d+)/book$', views.book, name="book"),
    re_path(r'flight/(?P<flight_id>\d+)/book/save$', views.save_booking, name="save_booking"),
    re_path(r'flight/(?P<user_id>\d+)/(?P<flight_id>\d+)/cancel$', views.cancel_booking, name="cancel_booking"),
]
