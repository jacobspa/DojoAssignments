from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    if 'id' in request.session:
        context = {
                'user': User.objects.get(id=request.session['id']),
                'books': Book.objects.all()
        }
        return render(request, 'reviews/index.html', context)
    else:
        return redirect('validate:home')

def books(request):
    return render(request, 'reviews/books.html')

def add(request):
    title = request.POST['html_title']
    author = request.POST['html_author']
    review = request.POST['html_review']
    rating = request.POST['html_rating']
    book = Book.objects.create(title=title, user_id=request.session['id'], author=author)
    Review.objects.create(review=review, rating=rating, poster_id=request.session['id'], book=book)
    book_id = Book.objects.get(title=title).id
    return redirect(reverse('review:reviews',kwargs={'book_id':book_id}))

def reviews(request, book_id):
    return render(request, 'reviews/book_review.html')

def users(request, user_id):
    pass

# Create your views here.
