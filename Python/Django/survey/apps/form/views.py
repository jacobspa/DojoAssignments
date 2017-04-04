from django.shortcuts import render,redirect, HttpResponse

def index(request):
    return render(request, 'form/survey.html')

def process(request):
    if request.method == 'POST':
        if 'count' not in request.session:
            request.session['count'] = 0
        request.session['count'] += 1
        request.session['name'] = request.POST['html_name']
        request.session['location'] = request.POST['html_location']
        request.session['lang'] = request.POST['html_lang']
        request.session['comment'] = request.POST['html_comment']
        return redirect('/results')

def results(request):
    return render(request, 'form/results.html')


# Create your views here.
