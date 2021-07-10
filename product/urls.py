from django.urls import path
from .views import Product
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('products_page/', Product.as_view(), name='products_page')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)