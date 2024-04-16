from django.urls import path
from .views import *

urlpatterns = [
    path('', BusBookingCreate.as_view()),
    path("list/", BusBookingList.as_view()),
    path("detail/<pk>/", BusBookingDetail.as_view()),
    path("update/<pk>/", BusBookingUpdate.as_view()),
    path("delete/<pk>/", BusBookingDelete.as_view()),

]
