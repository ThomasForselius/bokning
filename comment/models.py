from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from booking.models import Booking

class Comment(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="owner")
    receiver = models.OneToOneField(User, on_delete=models.CASCADE, related_name="receiver", default=None)
    text = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self): 
        return f' Booking: {Booking.date}, Comment by {self.owner}'