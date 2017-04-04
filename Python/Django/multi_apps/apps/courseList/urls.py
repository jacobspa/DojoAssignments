from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^add_course$', add, name ='add'),
    url(r'^remove/(?P<id>\d+)$', remove, name='remove')
]
