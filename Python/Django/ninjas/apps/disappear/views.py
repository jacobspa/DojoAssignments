from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'disappear/turtles.html')

def turtles(request):
    return redirect('/')


# Create your views here.
