import random
from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator


def index(request):

    catalog = list(Book.objects.all())
    random.shuffle(catalog)
    
    book_of_day = random.choice(catalog)

    return render(
        request,
        'index.html',
        {
            'book_of_day': book_of_day,
            'catalog': catalog}
    )


def catalog(request):
    
    # Set up Pagination
    p = Paginator(Book.objects.all(), 3)
    page = request.GET.get('page')
    books = p.get_page(page)

    return render(
        request,
        'catalog.html',
        {
            'catalog': catalog,
            'books': books
        }
    )


def contact(request):

    return render(
        request,
        'contact.html',
        {}
    )


def single(request, book_title):

    book = Book.objects.get(title=book_title)

    return render(
        request,
        'single.html',
        {
            "book": book
        }
    )


def checkout(request):

    return render(
        request,
        'checkout.html',
        {}
    )

def search(request):

    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()

    return render(
        request, 
        'search.html', 
        {'books': books}
    )

def cart(request):

    return render(
        request,
        'cart.html',
        {}
    )
