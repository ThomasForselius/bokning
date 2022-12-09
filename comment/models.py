from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from booking.models import Booking

class Comment(models.Model):
    booking = models.ForeignKey(Booking,
                             on_delete=models.CASCADE,
                             related_name='booking')
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    desc = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self): 
        return f' Booking: {self.booking.date}, Comment by {self.owner}'