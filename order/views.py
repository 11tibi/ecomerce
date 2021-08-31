from django.db.models import Sum, F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from accounts.models import ShoppingCart
from .models import City
from .forms import CheckoutForm


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
            'form': CheckoutForm(),
        }
        return render(request, 'cart/checkout.html', context)

    def post(self, request):
        pass


@method_decorator(csrf_exempt, name='dispatch')
class SelectCity(View):
    def post(self, request):
        try:
            cities = City.objects.filter(county=request.POST.get('county_id')).order_by('city')
            context = {'cities': cities}
            html = render_to_string('cart/select city.html', context)
            return JsonResponse({'html': html}, status=200)
        except ValueError:
            return JsonResponse({}, status=404)


@method_decorator(csrf_exempt, name='dispatch')
class SelectCustomer(View):
    def post(self, request):
        try:
            html = render_to_string('cart/customer type.html')
            return JsonResponse({'html': html}, status=200)
        except ValueError:
            return JsonResponse({}, status=404)

# https://getbootstrap.com/docs/4.0/examples/checkout/
# https://bbbootstrap.com/snippets/bootstrap-ecommerce-shopping-cart-item-summary-44021562
# https://bbbootstrap.com/snippets/bootstrap-ecommerce-checkout-page-payment-options-50848752

# https://github.com/byteweaver/django-coupons
