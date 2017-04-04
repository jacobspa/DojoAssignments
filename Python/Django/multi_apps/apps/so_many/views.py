from django.shortcuts import render

def index(request):
    return render(request, 'so_many/index.html')
# Create your views here.
