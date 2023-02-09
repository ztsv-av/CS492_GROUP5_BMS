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
    quantity = cart.get_item(book_id)
    
    if quantity:
        quantity = quantity['quantity']

        item = {
            'book': {
                'bookID': book.bookID,
                'title': book.title,
                'image': book.image,
                'description': book.description,
                'genre': book.genre,
                'price': book.price,
            },
            'total_price': (int(quantity) * int(book.price)),
            'quantity': int(quantity),
        }
    else:
        item = None

    response = render(
        request, 
        'cart/cart_item.html',
        {'item': item}
    )
    response['HX-Trigger'] = 'update-menu-cart'

    return response


@login_required
def checkout(request):
    
    return render(request, 'cart/checkout.html')


def hx_menu_cart(request):
    return render(request, 'cart/menu_cart.html')


def hx_cart_total(request):
    return render(request, 'cart/cart_total.html')

