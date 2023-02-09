from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .cart import Cart
from website.models import Book


def add_to_cart(request, book_id):

    cart = Cart(request)
    cart.add(book_id)

    return render(
        request,
        'menu_cart.html'
    )


def cart(request):

    return render(request, 'cart.html')


def update_cart(request, book_id, action):

    cart = Cart(request)

    if action == 'increment':
        cart.add(book_id, 1, True)
    else:
        cart.add(book_id, -1, True)
    
    book = Book.objects.get(pk=book_id)
    quantity = cart.get_item(book_id)['quantity']
    
    # if quantity:
    #     quantity = quantity['quantity']

    item = {
        'book': {
            'id': book.id,
            'title': book.title,
            'image': book.image,
            'description': book.description,
            'genre': book.genre,
            'price': book.price,
        },
        'total_price': round(float(book.price) * int(quantity), 2),
        'quantity': int(quantity),
    }
    # else:
    #     item = None

    response = render(
        request, 
        'cart_item.html',
        {'item': item}
    )
    response['HX-Trigger'] = 'update-menu-cart'

    return response


@login_required
def checkout(request):
    
    return render(request, 'checkout.html')


def hx_menu_cart(request):
    return render(request, 'menu_cart.html')


def hx_cart_total(request):
    return render(request, 'cart_total.html')

