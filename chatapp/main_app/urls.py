from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('chatapp/myhome', views.myhome, name='myhome'),
    path('chatapp/<int:channel_id>', views.message_in_channel, name='myhome'),
]
