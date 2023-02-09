from django.contrib import admin
from django.urls import path, include
from cart.views import cart, add_to_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('members.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('cart/', include('cart.urls')),
    path('', include('website.urls')),
]
