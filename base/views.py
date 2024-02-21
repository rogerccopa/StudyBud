from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

def home(request):
    # context = {'rooms': rooms}
    context = {'rooms': Room.objects.all()}
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
