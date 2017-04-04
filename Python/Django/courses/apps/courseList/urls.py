from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^add_course$', add),
    url(r'^remove/(?P<id>\d+)$', remove)
]
