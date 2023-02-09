from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
    # path('update_cart/<int:book_id>/<str:action>.', views.update_cart, name='update_cart'),
    # path('hx_menu_cart', views.hx_menu_cart, name='hx_menu_cart'),
    # path('hx_cart_total', views.hx_cart_total, name='hx_cart_total'),

]
