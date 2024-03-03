from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q  # Q allows to use and/or to filter objects
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from pprint import pprint

from .models import Room, Topic
from .forms import RoomForm

def loginPage(request):
    if request.method == 'POST':
        un = request.POST.get('username')
        pw = request.POST.get('password')

        user = User.objects.filter(username = un)

        if not user.exists():
            messages.error(request, 'User does not exist')
        else:
            user = authenticate(request, username=un, password=pw)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'User or password does not exist')
            
    context = {}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    # double underscore allows access to the related table's fields
    # also, allows to use comparison functions
    rooms = Room.objects.filter(
        Q(topic__name__contains = q) |  # &=and |=or
        Q(name__icontains = q) |        # icontains -> (<i>gnore-case)
        Q(description__icontains = q)
    )
    room_count = rooms.count()
    topics = Topic.objects.all()
    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
    return render(request, 'base/home.html', context)

def room (request, pk):
    selectedRoom = Room.objects.get(id = pk)
    context = {'room': selectedRoom}

    return render(request, 'base/room.html', context)

def createRoom(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    form = RoomForm()
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id = pk)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    form = RoomForm(instance=room)
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id = pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    
    return render(request, 'base/delete.html', {'obj': room})
