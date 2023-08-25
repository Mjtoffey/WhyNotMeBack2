from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone
from django.conf import settings

class CustomUser(AbstractUser):
     def __str__(self):
        return self.username
    # # your custom fields and methods
    
    # class Meta:
    #     swappable = "AUTH_USER_MODEL"

    # # Add related_name to groups and user_permissions fields
    # groups = models.ManyToManyField(
    #     Group,
    #     verbose_name=('groups'),
    #     blank=True,
    #     help_text=('The groups this user belongs to.'),
    #     related_name='custom_users_group'  # Use a unique related_name
    # )
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     verbose_name=('user permissions'),
    #     blank=True,
    #     help_text=('Specific permissions for this user.'),
    #     related_name='custom_users_permission'  # Use a unique related_name
    # )

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
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_nbr = models.CharField(max_length=20)
    social_media = models.CharField(max_length=255)
    sport = models.CharField(max_length=255)
    player = models.BooleanField(default=False)
    school = models.CharField(max_length=255)

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