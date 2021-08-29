from django.contrib.auth.decorators import login_required
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Cart, Checkout

urlpatterns = [
    path('', login_required(Cart.as_view()), name='cart'),
    path('detalii-comanda', login_required(Checkout.as_view()), name='checkout'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)