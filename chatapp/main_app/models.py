from django.db import models
from datetime import date

# Import the User
from django.contrib.auth.models import User
# Create your models here.


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

    def __str__(self):
        return self.name
