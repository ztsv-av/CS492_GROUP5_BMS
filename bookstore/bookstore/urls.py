from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('cart/', include('cart.urls')),
    path('members/', include('members.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
]
