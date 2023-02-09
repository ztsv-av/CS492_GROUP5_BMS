from .cart import Cart


# make cart globally available
def cart(request):

    return {'cart': Cart(request)}
