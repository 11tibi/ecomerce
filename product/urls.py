from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import Products, ProductsPage, ProductPage, AddReview, DeleteReview, AddToCart, DeleteCartItem
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('delete-review', login_required(DeleteReview.as_view()), name='delete-review'),
    path('add-cart', AddToCart.as_view(), name='add_to_cart'),
    path('delete-cart-item', login_required(DeleteCartItem.as_view()), name='delete_cart_item'),
    path('review/<slug:product>', login_required(AddReview.as_view()), name='add_review'),
    path('<str:category>', Products.as_view(), name='products'),
    path('<slug:category>/<str:page>', ProductsPage.as_view(), name='products_page'),
    path('<slug:category>/<slug:product>/<slug:product_code>', ProductPage.as_view(), name='product'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
