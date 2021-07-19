from django.urls import path
from .views import Products, ProductsPage, ProductPage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<str:category>', Products.as_view(), name='products'),
    path('<slug:category>/<str:page>', ProductsPage.as_view(), name='products_page'),
    path('<slug:category>/<slug:product>/<slug:product_code>', ProductPage.as_view(), name='product'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
