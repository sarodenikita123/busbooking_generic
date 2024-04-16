from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import BusBooking


class BusBookingCreate(CreateView):
    model = BusBooking
    fields = "__all__"


class BusBookingList(ListView):
    model = BusBooking


class BusBookingDetail(DetailView):
    model = BusBooking


class BusBookingUpdate(UpdateView):
    model = BusBooking
    fields = "__all__"
    success_url = "/"


class BusBookingDelete(DeleteView):
    model = BusBooking
    success_url = "/"
    template_name = "crud_app/busbooking_delete.html"


