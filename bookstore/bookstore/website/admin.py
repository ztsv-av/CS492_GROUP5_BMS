from django.contrib import admin
from .models import Book
from .models import Order
from .models import User

admin.site.register(Book)
admin.site.register(Order)
admin.site.register(User)