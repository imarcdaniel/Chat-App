from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('chatapp/myhome', views.myhome, name='myhome'),
    path('chatapp/new', views.channel_new, name='new_channel'),
    path('channels/submit/', views.channel_create, name='create_channel'),
    path('chatapp/channels/<int:channels_id>/',
         views.load_channel, name='view_channel'),
    path('chatapp/channels/<int:channels_id>/',
         views.load_message, name='view_channel'),

]
