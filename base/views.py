from django.shortcuts import render
from .models import Room

rooms = [
    {'id':1, 'name':'Lets learn python'},
    {'id':2, 'name':'Disign with me'},
    {'id':3, 'name':' Frontend developers'}
]

def home(request):
    # context = {'rooms': rooms}
    context = {'rooms': Room.objects.all()}
    return render(request, 'base/home.html', context)

def room (request, pk):
    selectedRoom = None

    for room in rooms:
        if room['id'] == int(pk):
            selectedRoom = room
    
    context = {'room': selectedRoom}

    return render(request, 'base/room.html', context)
