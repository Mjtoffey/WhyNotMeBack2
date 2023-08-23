from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    def __str__(self):
        return self.email
    
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class UserLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class School(models.Model):
    school_name = models.CharField(max_length=255)
    school_type = models.CharField(max_length=255)

class User(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_nbr = models.CharField(max_length=20)
    social_media = models.CharField(max_length=255)
    sport = models.CharField(max_length=255)
    player = models.BooleanField(default=False)

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