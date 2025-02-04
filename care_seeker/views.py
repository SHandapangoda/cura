from django.shortcuts import render, get_object_or_404
from .models import Booking

def book_care_provider(request):
    if request.method == 'POST':
        # Handle booking logic
        pass
    return render(request, 'care_seeker/book.html')

def track_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'care_seeker/track.html', {'booking': booking})