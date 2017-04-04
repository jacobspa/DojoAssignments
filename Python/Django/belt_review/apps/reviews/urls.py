from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name= 'home'),
    url(r'^books/add$', books, name='books'),
    url(r'^add$', add, name='add'),
    url(r'^books/(?P<user_id>\d+)$', reviews, name='reviews'),
    url(r'^users/(?P<id>\d+)$', users, name='users')
]
