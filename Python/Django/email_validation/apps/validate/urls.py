from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^login$', login),
    url(r'^register$', register),
    url(r'^success$', success)
]
