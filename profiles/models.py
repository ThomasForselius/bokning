from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(max_length=1000, blank=True)
    age = models.IntegerField(blank=True, default=18)
    image = models.ImageField(upload_to='bokning/', default='profile_circle_cd6xw6.svg', blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"

def create_profile(sender, instance, created, **kwargs):
    if created: Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)