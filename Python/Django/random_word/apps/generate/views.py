from django.shortcuts import render, HttpResponse
import random

def index(request):
    if 'attempts' not in request.session:
        request.session['attempts'] = 0
    # x = ['a','b','c','e','q','p','e','e','e','t','w','r']
    request.session['attempts'] += 1
    # data = {
    # # 'num':  x.random()
    # }
    return render(request,'generate/random.html' )

# Create your views here.
