from django.shortcuts import render, HttpResponse
from datetime import datetime

def index(request):

    return render(request,'timedisplay/display_time.html', {'time': datetime.now()})

# Create your views here.
