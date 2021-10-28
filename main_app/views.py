from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Channel, Contact, Message, User
from django.utils import timezone
# from django.views.generic import DeleteView
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


def channel_edit(request, channels_id):
    editchannel = Channel.objects.get(id=channels_id)
    return render(request, 'channels/edit.html', {'channel': editchannel})


def channel_update(request, channels_id):
    updatechannel = Channel.objects.get(id=channels_id)
    updatechannel.name = request.POST['name']
    updatechannel.save()
    channels = Channel.objects.all
    return render(request, 'channels/index.html', {'channels': channels})


def load_channel(request, channels_id):
    channel = Channel.objects.get(id=channels_id)
    messages = Message.objects.filter(
        channel_id=channels_id).order_by('date').values()
    messagesdetail = []
    for m in messages:
        userobject = User.objects.get(id=m['user_id'])
        case = {"id": m['user_id'], "username": userobject.username,
                "body": m['body'], "date": m['date']}
        messagesdetail.append(case)

    return render(request, 'channels/detail.html', {"messages": messages, "channel": channel, "messagesdetail": messagesdetail})


def message_create(request):
    newmessage = Message.objects.create(
        body=request.POST["body"],
        channel_id=request.POST['channel_id'],
        user_id=request.user.id,
        date=timezone.now
    )
    return redirect(request.META['HTTP_REFERER'])


def message_delete(request, message_id):
    del_message = Message.objects.get(id=message_id)
    del_message.delete()
    return redirect(request.META['HTTP_REFERER'])


def channel_detail(request):
    return render(request, 'channels/detail.html')


def add_a_contact(request, clicked_user_id, current_user_id):
    current_user_id = request.user.id,
    clicked_user_id = User.objects.get(id=clicked_user_id).id
    Contact.objects.get(id=current_user_id).users.add(clicked_user_id)
    return redirect('detail', current_user_id=current_user_id)
    # def message_in_channel(request):
    #   print("this the channel", channels)
    # return render(request, 'channels/index.html', {"channels": channels})


def load_contacts(request):
    contacts = Contact.objects.filter(
        creator_id=request.user.id).select_related("friend_set").values()

    contactdetail = []
    for c in contacts:
        userobject = User.objects.get(id=c['creator_id'])
        contactobject = User.objects.get(id=c['contact_id'])
        case = {"id": c['contact_id'], "contactusername": contactobject.username, "contactfirstname": contactobject.first_name, "contactlastname": contactobject.last_name, "contactemail": contactobject.email,
                "creatorusername": userobject.username, "date": c['created']}
        contactdetail.append(case)

    return render(request, 'contacts/all.html', {"contacts": contacts,  "contactdetail": contactdetail})
