from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone
from django.conf import settings

class CustomUser(AbstractUser):
    def __str__(self):
        return self.email
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)

class UserLog(models.Model):
    # other fields
    
    # Update the user_id field to point to settings.AUTH_USER_MODEL
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_logs'
    )

    # other fields

    def __str__(self):
        return f"User Log for {self.user}"

class User(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    phone_nbr = models.CharField(max_length=20)
    social_media = models.CharField(max_length=255)
    sport = models.CharField(max_length=255)
    player = models.BooleanField(default=False)
    school = models.CharField(max_length=255)
    date_registered = models.DateTimeField(default=timezone.now)

class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    win = models.BooleanField(default=True)
    points = models.IntegerField(default=0)
    rebounds = models.IntegerField(default=0)
    blocks = models.IntegerField(default=0)
    steals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    saves = models.IntegerField(default=0)
    min_played = models.IntegerField(default=0)


class UserProfile(models.Model):
    school = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_nbr = models.CharField(max_length=20)
    social_media = models.CharField(max_length=100)
    sport = models.CharField(max_length=50)
    player = models.BooleanField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"