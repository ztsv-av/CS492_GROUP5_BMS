from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('members.urls')),
    path('', include('website.urls')),
    path('members/', include('django.contrib.auth.urls')),
]
