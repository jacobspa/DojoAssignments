from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name='manager'),
    url(r'^add$', add_playlist, name='add_playlist'),
    url(r'^add_song/(?P<playlist_id>\d+)$', add_song, name='add_song'),
]
