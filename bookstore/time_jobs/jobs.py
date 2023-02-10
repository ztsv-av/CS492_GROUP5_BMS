from django.conf import settings
import requests
import json
import random
from website.models import MfgInventory, Book


def check_book():

    books = list(Book.objects.all())

    for book in books:

        quantity = int(book.quantity)

        if quantity < 5:

            book_mfg = MfgInventory.objects.get(pk=book.id)

            if book_mfg.quantity > 20:
                book_mfg.quantity -= 20
                book.quantity += 20
            
            elif book_mfg.quantity > 0:
                book.quantity += book_mfg.quantity
                book_mfg.quantity = 0
            
            else:
                book_mfg.available = 0
                print('Book ' + book.title + ' is unavailable to order from the manufacturer!')
            
            book.save()
            book_mfg.save()

            print('Book ID:' + str(book.id) + '; Title: ' + book.title + ' was ordered from the manufacturers!')
