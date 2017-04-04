from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
import re

def index(request):
    return render(request, 'validate/index.html')

def login(request):
    is_valid = True
    if not User.objects.email_validate(request.POST['html_email']):
        messages.error(request, 'Invalid email!')
        is_valid = False
    if User.objects.get(email = request.POST['html_email']).password != request.POST['html_password']:
        messages.error(request, 'Password is incorrect!')
        is_valid = False
    if is_valid:
        return redirect('/success')



def register(request):
    is_valid = True
    if len(request.POST['html_email']) < 4:
        messages.add_message(request,messages.ERROR,'Email must be at least 4 characters!')
        is_valid = False
    if len(request.POST['html_first']) < 2:
        messages.add_message(request,messages.ERROR, 'First Name must be at least 3 characters!')
        is_valid = False
    if len(request.POST['html_last']) <2:
        messages.add_message(request,messages.ERROR, 'Last name must be at least 3 characters!')
        is_valid = False
    if not User.objects.email_validate(request.POST['html_email']):
        messages.add_message(request,messages.ERROR, 'Invalid email!')
        is_valid = False
    if not User.objects.pw_validate(request.POST['html_password'], request.POST['html_confirm']):
        messages.add_message(request,messages.ERROR, "passwords don't match")
        is_valid = False
    if is_valid:
        User.objects.create(email = request.POST['html_email'], first_name=request.POST['html_first'], last_name=request.POST['html_last'], password=request.POST['html_password'])
        return redirect('/success')
    else:
        return redirect('/')

def success(request):
        context = {
                'Users': User.objects.all()
                }
        return render(request, 'validate/success.html', context)


# Create your views here.
