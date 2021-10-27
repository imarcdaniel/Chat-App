from datetime import date
from django.db import models

# Import the User
from django.contrib.auth.models import User
# Create your models here.

class Message(models.Model):
   body = models.CharField(max_length=150)
   date = models.DateField(auto_now_add=True)

def __str__(self):
    return self.body
