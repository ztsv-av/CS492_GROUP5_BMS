from django.conf import settings
import requests
import json
import random
from website.models import MfgInventory, Book


def check_book():

    books = list(Book.objects.all())

    for book in books:

        book_quantity = int(book.quantity)

        if book_quantity < 5:

            book_mfg = MfgInventory.objects.get(pk=book.id)
            mfg_quantity = int(book_mfg.quantity)

            if mfg_quantity > 10:
                mfg_quantity -= 10
                book_quantity += 10

                print('Book ' + book.title + ' was ordered from the manufacturers!\n')
            
            elif mfg_quantity > 0:
                book_quantity += mfg_quantity
                mfg_quantity = 0
                book_mfg.available = 0

                print('Book ' + book.title + ' was ordered from the manufacturers!')
                print('Cannot order ' + book.title + ' from the manufacturer!\n')
            
            else:
                book_mfg.available = 0
                print('Cannot order ' + book.title + ' from the manufacturer!\n')

            if book_quantity == 0:
                print('Book ' + book.title + ' is unavailable!\n')
                book.available = 0

            book.quantity = str(book_quantity)
            book_mfg.quantity = str(mfg_quantity)
            
            book.save()
            book_mfg.save()
