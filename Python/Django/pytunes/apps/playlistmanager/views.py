from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

def index(request):
    context = {
            'title': 'The Worlds greatest playlist manager',
            'playlists': Playlist.objects.all()
    }
    return render(request,'playlistmanager/index.html', context)

def add_playlist(request):
    name = request.POST['playlist_name']
    try:
        Playlist.objects.create(name=name, rating=0)
    except:
        messages.error(request, 'Name is duplicate. Do not be such a Mark!!')
    return redirect('playlist:manager')

def add_song(request, playlist_id):
    if request.method =='POST':
        title = request.POST['song_name']
        try:
            Song.objects.create(title=title)
        except:
            message.error(request, 'Song title is a duplicate. Do not be such a MARK!!!')
        return redirect('playlist:manager')
    context = {
            'playlist': Playlist.objects.get(id=playlist_id)
    }
    return render(request, 'playlistmanager/songs.html', context)
def song_display(request):
    return render('playlistmanager/songs.html')
