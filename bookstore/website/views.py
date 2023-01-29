import random
from django.shortcuts import render
from .models import Book

def index(request):

    catalog = list(Book.objects.all())
    book_of_day = random.choice(catalog)

    return render(
        request,
        'index.html',
        {
            'book_of_day': book_of_day,
            'catalog': catalog}
    )


def catalog(request):

    return render(
        request,
        'catalog.html',
        {}
    )


def contact(request):

    return render(
        request,
        'contact.html',
        {}
    )


def single(request):

    book_list = Book.objects.all()


    return render(
        request,
        'single_book.html',
        {"book_list": book_list}
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
        books = Book.objects.filter(name__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'catalog.html', {'books': books})