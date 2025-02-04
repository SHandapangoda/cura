from django.urls import path
from . import views

urlpatterns = [
    path('bookings/', views.view_bookings, name='view_bookings'),
    path('accept-booking/<int:booking_id>/', views.accept_booking, name='accept_booking'),
]