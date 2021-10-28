from django.db import models
from datetime import date


# Import the User
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=150, default=SET_NULL)

    def __str__(self):
        return f"{self.name}"


class Message(models.Model):
    body = models.CharField(max_length=150)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey('Channel', on_delete=models.CASCADE)

    def __str__(self):
        return self.body


class Channel(models.Model):
    name = models.CharField(max_length=150)
    creationdate = models.DateField(auto_now_add=True)
    messages = models.ForeignKey(
        Message, blank=True, null=True, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Contact(models.Model):
    created = models.DateField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="contact_creator_set")
    contact = models.ForeignKey(
        User, blank=True, null=True, related_name="friend_set", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.creator}"
