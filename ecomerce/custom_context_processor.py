from django.db.models import Sum, F
from product.models import Categories
from accounts.models import ShoppingCart


def category_renderer(request):
    return {
        'all_categories': Categories.objects.all(),
        'count_all_categories': Categories.objects.count(),
    }


def shopping_cart(request):
    if request.user.is_authenticated:
        cart = ShoppingCart.objects.select_related('product', 'product__category').filter(user=request.user.id)
        total_price = ShoppingCart.objects.select_related('product').filter(user=request.user.id).aggregate(
            total_price=Sum(F('product__price') * F('quantity')), count=Sum(F('quantity')))
        return {
            'cart': cart,
            'total_price': total_price['total_price'],
            'count': total_price['count'],
        }
