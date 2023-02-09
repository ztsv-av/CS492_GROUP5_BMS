from django.shortcuts import render, redirect

from cart.cart import Cart

from .models import Order, OrderItem

def start_order(request):

    cart = Cart(request)

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        zipcode = request.POST.get('zipcode')
        place = request.POST.get('place')
        phone = request.POST.get('phone')

        order = Order.objects.create(
            user=request.user, 
            first_name=first_name, 
            last_name=last_name, 
            email=email, 
            phone=phone, 
            address=address, 
            zipcode=zipcode, 
            place=place)

        for item in cart:
            book = item['book']
            quantity = int(item['quantity'])
            price = float(book.price) * int(quantity)

            item = OrderItem.objects.create(
                order=order,
                book=book, 
                price=price, 
                quantity=quantity)

        return redirect('index')

    return redirect('cart')
