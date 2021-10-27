from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('chatapp/myhome', views.myhome, name='myhome'),
    path('myhome/<int:channel_id', views.channel_detail, name="channel")

]
