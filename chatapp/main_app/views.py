from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Channel, Friend, Message, User
from django.utils import timezone
# Create your views here.


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        print(' step1')
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            print('we are in the first if statement')
            login(request, user)
            print('it should hit redirect now')
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def myhome(request):
    channels = Channel.objects.all
    print("These are the user channels", channels)
    return render(request, 'channels/index.html', {'channels': channels})


def channel_new(request):
    return render(request, 'channels/new.html', {})


def channel_create(request):
    createchannel = Channel.objects.create(
        name=request.POST['name'],
        creationdate=request.POST['date'],
    )
    return redirect(f'/chatapp/channels/{createchannel.id}')


def load_channel(request, channels_id):
    channel = Channel.objects.get(id=channels_id)
    messages_of_loggeg_in_user = Message.objects.filter(
        channel_id=channels_id).filter(user_id=request.user)
    messages_of_other_user = Message.objects.filter(
        channel_id=channels_id).exclude(user_id=request.user)
    print(channel)
    return render(request, 'channels/detail.html', {"messages_home": messages_of_loggeg_in_user, "messages_away": messages_of_other_user, "channel": channel})


def message_create(request):
    newmessage = Message.objects.create(
        body=request.POST["body"],
        channel_id=request.POST['channel_id'],
        user_id=request.user.id,
        date=timezone.now
    )
    return redirect(request.META['HTTP_REFERER'])


def channel_detail(request):
    return render(request, 'channels/detail.html')

def add_a_contact(request, clicked_user_id, current_user_id):
  current_user_id = request.user.id,
  clicked_user_id = User.objects.get(id=clicked_user_id).id
  Friend.objects.get(id=current_user_id).users.add(clicked_user_id)
  return redirect('detail', current_user_id=current_user_id)
    # def message_in_channel(request):
    #   print("this the channel", channels)
    # return render(request, 'channels/index.html', {"channels": channels})
