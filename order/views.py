from django.db.models import Sum, F
from django.shortcuts import render
from django.views import View
from product.models import Product
from accounts.models import ShoppingCart


class Cart(View):
    def get(self, request):
        total_price = ShoppingCart.objects.select_related('product').filter(user=request.user.id).aggregate(
            total_price=Sum(F('product__price') * F('quantity')), count=Sum(F('quantity')))
        cart = ShoppingCart.objects.select_related('product', 'product__category').filter(user=request.user.id)
        context = {
            'total_price': total_price['total_price'],
            'count': total_price['count'],
            'cart': cart,
        }
        return render(request, 'cart/cart.html', context)

    def post(self, request):
        pass


class Checkout(View):
    def get(self, request):
        context = {

        }
        return render(request, 'cart/checkout.html', context)

    def post(self, request):
        pass

# https://getbootstrap.com/docs/4.0/examples/checkout/
# https://bbbootstrap.com/snippets/bootstrap-ecommerce-shopping-cart-item-summary-44021562
# https://bbbootstrap.com/snippets/bootstrap-ecommerce-checkout-page-payment-options-50848752

# https://github.com/byteweaver/django-coupons
