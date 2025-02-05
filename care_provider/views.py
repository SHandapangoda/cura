from django.shortcuts import get_object_or_404, redirect
from care_seeker.models import Booking
from django.contrib import messages

def reject_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, care_provider__user=request.user)
    booking.status = "REJECTED"
    booking.save()
    messages.warning(request, "You have rejected this booking.")
    return redirect('view_bookings')
