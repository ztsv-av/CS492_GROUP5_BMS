from django.contrib import admin
from django.urls import path, include
from cart.views import add_to_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('members.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('add_to_cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('', include('website.urls')),
]
