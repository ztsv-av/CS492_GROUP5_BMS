from django.conf import settings
import requests
import json
import random
from ast import literal_eval
from website.models import MfgInventory, Book


def check_book():

    books = list(Book.objects.all())

    for book in books:

        quantity = literal_eval(book.quantity)

        if quantity < 5:

            print('Need to Order ' + book.title + ' from manufacturers!')

        if quantity == 0:
            book.available == 0
            book.save()

            print('Book ' + book.title + ' is unavailable in inventory!')


def check_mfg():

    mfg = list(MfgInventory.objects.all())

    for book in mfg:

        quantity = literal_eval(book.quantity)

        if quantity == 0:
            book.available = 0
            book.save()

            print('Book ' + book.title + ' is unavailable from the manufacturer!')