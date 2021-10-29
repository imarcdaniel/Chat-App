from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('chatapp/myhome', views.myhome, name='myhome'),
    path('chatapp/new', views.channel_new, name='new_channel'),
    #
    path('channels/submit/', views.channel_create, name='create_channel'),
    path('chatapp/channels/<int:channels_id>/',
         views.load_channel, name='view_channel'),
    path('chatapp/channels/<int:message_id>/delete',
         views.message_delete, name='del_message'),

    path('chatapp/channels/submit_message/',
         views.message_create, name='new_message'),
    path('chatapp/channels/<int:channels_id>/edit/',
         views.channel_edit),
    path('chatapp/channels/<int:channels_id>/submit_update_form/',
         views.channel_update),
    path('chatapp/channels/<int:message_id>/delete',
         views.message_delete, name='del_message'),

    path('myhome/<int:channels_id>/', views.channel_detail, name="channel"),
    path('chatapp/contacts', views.load_contacts, name='contacts'),
    path('chatapp/channels/<int:channels_id>/edit',
         views.channel_edit, name='edit_channel'),
    path('chatapp/channels/<int:channels_id>/update/',
         views.channel_update, name='update_channel'),
]
