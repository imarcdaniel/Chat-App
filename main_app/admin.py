from django.contrib import admin
from .models import Channel, Message, Contact, UserProfile
# Register your models here.

admin.site.register(Channel)
admin.site.register(Message)
admin.site.register(Contact)
admin.site.register(UserProfile)
