import csv
from django.contrib import admin
from .models import Book, User, MfgInventory
from django.http import HttpResponse
from django.db import models
from ast import literal_eval


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'price', 'available', 'quantity']


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'email', 'phone']


class MfgAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'available', 'quantity']
   

admin.site.register(Book, BookAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(MfgInventory, MfgAdmin)
