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