import csv
from django.contrib import admin
from .models import Order
from django.http import HttpResponse


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
            total_sales += float(order.paid_amount)
            quantity += 1
            writer.writerow(['', '', order])
        writer.writerow([total_sales, quantity])

        return response

get_sales_record.short_description = 'Create Sales Record'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['email', 'paid_amount', 'created_at', 'status']
    actions = [get_sales_record]


admin.site.register(Order, OrderAdmin)
