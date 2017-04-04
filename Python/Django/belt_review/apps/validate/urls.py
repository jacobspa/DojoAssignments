from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^login$', login, name='login'),
    url(r'^register$', register, name='register'),
    url(r'^success$', success),
    url(r'^logout$', logout, name='logout')
]
