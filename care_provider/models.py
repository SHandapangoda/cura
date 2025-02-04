from django.db import models
from users.models import User

class CareProvider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='care_provider')
    experience = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    tasks = models.JSONField(default=list)  # List of tasks they can perform
    is_available = models.BooleanField(default=True)