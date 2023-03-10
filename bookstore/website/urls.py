from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('catalog', views.catalog, name='catalog'),
    path('contact', views.contact, name='contact'),
    path('single/<book_title>', views.single, name='single'),
    path('search', views.search, name='search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
