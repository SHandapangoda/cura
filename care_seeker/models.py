from django.db import models
from users.models import User

class CareSeeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='care_seeker')
    preferences = models.JSONField(default=dict)  # Store preferences like gender, language, etc.

class Booking(models.Model):
    care_seeker = models.ForeignKey(CareSeeker, on_delete=models.CASCADE, related_name='bookings')
    care_provider = models.ForeignKey('care_provider.CareProvider', on_delete=models.CASCADE)
    tasks = models.JSONField(default=list)  # List of tasks like "Prepare breakfast", "Give medicine"
    status = models.CharField(max_length=20, default='PENDING')  # PENDING, ACCEPTED, COMPLETED
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def send_booking_status_email(sender, instance, **kwargs):
    if instance.status in ["ACCEPTED", "REJECTED", "COMPLETED"]:
        send_mail(
            f'Your Booking Status: {instance.status}',
            f'Your booking with {instance.care_provider.user.first_name} is now {instance.status}.',
            'admin@cura.com',
            [instance.care_seeker.user.email],
        )
        