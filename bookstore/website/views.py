import random
from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator


def index(request):

    catalog = list(Book.objects.all())
    nonfiction_catalog = Book.objects.filter(genre__icontains="Nonfiction")
    manga_catalog = Book.objects.filter(genre__icontains="Manga")
    horror_catalog = Book.objects.filter(genre__icontains="Horror")
    adventure_catalog = Book.objects.filter(genre__icontains="Adventure")
    fiction_catalog = Book.objects.filter(genre__icontains="Fiction")
    random.shuffle(catalog)
    
    book_of_day = random.choice(catalog)

    return render(
        request,
        'index.html',
        {
            'book_of_day': book_of_day,
            'nonfiction_catalog': nonfiction_catalog,
            'manga_catalog': manga_catalog,
            'horror_catalog': horror_catalog,
            'adventure_catalog': adventure_catalog,
            'fiction_catalog': fiction_catalog,
            'catalog': catalog}
    )


def catalog(request):
    
    # Set up Pagination
    p = Paginator(Book.objects.all(), 6)
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


def single(request, book_title):

    book = Book.objects.get(title=book_title)

    return render(
        request,
        'single.html',
        {
            "book": book
        }
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


def contact(request):

    return render(
        request,
        'contact.html',
        {}
    )
