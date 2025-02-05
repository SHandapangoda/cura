from django.db import models
from users.models import User

class Query(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='queries')
    subject = models.CharField(max_length=255)
    message = models.TextField()
    status = models.CharField(max_length=20, default='OPEN')  # OPEN, IN_PROGRESS, CLOSED
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)