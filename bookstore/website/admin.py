import csv
from django.contrib import admin
from .models import Book, Order, User, MfgInventory
from django.http import HttpResponse
from django.db import models
from ast import literal_eval


def get_sales_record(modeladmin, request, queryset):

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=sales_record.csv'

        # csv writer
        writer = csv.writer(response)

        # designate the model
        orders = Order.objects.all()

        # add column headins to the csv file
        writer.writerow(['Total Sales', 'Quantity', 'History'])

        # add values to the csv file
        total_sales = 0
        quantity = 0
        for order in orders:
            total_sales += literal_eval(order.amount)
            quantity += 1
            writer.writerow(['', '', order])
        writer.writerow([total_sales, quantity])

        return response

get_sales_record.short_description = 'Create Sales Record'


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'available', 'num_available']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'date', 'successful']
    actions = [get_sales_record]


class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'password', 'phone']

class MfgAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'available', 'qty_available']
   


admin.site.register(Book, BookAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(MfgInventory, MfgAdmin)