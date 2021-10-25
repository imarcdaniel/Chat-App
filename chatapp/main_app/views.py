from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Channel
# Create your views here.

# class Channel:
#   def __init__(self, name, creationdate):
#     self.name = name
#     self.creationdate = creationdate

# channels = [
#   Channel('Sei43', 'today' ),
#   Channel('Sports', 'yesterday'),
#   Channel('News', 'last week',)
# ]


# class Message:
#   def __init__(self, body, datesent, user_id, channelid):
#     self.body = body
#     self.datesent = datesent
#     self.user = user_id
#     self.channelid= channelid


# messages = [
#     Message('Lorem Ipsum has been the industrys standard dummy text ever since the ', 'today', 'Test1'),
#     Message('it has survived not only five centuries, but also the leap into electronic typesetting', 'today', 'Test2'),
#     Message('remaining essentially unchanged. It was popularised in the 1960s',
#             'today', 'Test3')
# ]

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


def myhome(request):
    # channels = Channel.objects.all
    print("this the channel", channels)
    return render(request, 'channels/index.html', {"channels": channels})

    # def myhome(request):
    #   # channels = Channel.objects.all
    # print("this the channel", channels)
    # return render(request, 'channels/index.html', {"channels": channels})

    # def message_in_channel(request):
    #   print("this the channel", channels)
    # return render(request, 'channels/index.html', {"channels": channels})
