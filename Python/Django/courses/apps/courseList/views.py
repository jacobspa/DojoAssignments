from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    context = {
            'courses': Course.objects.all()
    }
    return render(request,'courseList/index.html', context)

def add(request):
    server_course = request.POST['html_course_name']
    server_description = request.POST['html_description']
    Course.objects.create(course_name=server_course, description=server_description)
    return redirect('/')

def remove(request, id):
    Course.objects.filter(id = id).delete()
    return redirect('/')
