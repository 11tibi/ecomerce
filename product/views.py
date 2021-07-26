from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, redirect
from django.views import View
from product.models import Product, Specs

# Create your views here.


class Products(View):
    def get(self, request, category):
        return redirect(f'{category}/page1')

    def post(self, request, category):
        pass


class ProductsPage(View):
    def get(self, request, category, page):
        paginator = Paginator(Product.objects.select_related('discount', 'category', 'inventory').filter(category__link=category).all(), 60)

        try:
            products = paginator.page(page[4:])
        except(EmptyPage, InvalidPage):
            products = paginator.page(1)

        index = products.number - 1
        max_index = len(paginator.page_range)
        start_index = index - 3 if index >= 3 else 0
        end_index = index + 3 if index <= max_index - 3 else max_index
        page_range = list(paginator.page_range)[start_index:end_index]

        context = {
            'products': products, 
            'page_range': page_range,
            'category': category,
        }

        return render(request, 'products/products.html', context)

    def post(self, request, category, page):
        pass


class ProductPage(View):
    def get(self, request, category, product, product_code):
        prod = Product.objects.select_related('discount', 'category', 'inventory').filter(category__link=category, link=product).all()
        specs = Specs.objects.select_related('prod').filter(prod__link=product).all()

        context = {
            'product': prod[0],
            'specs': specs,
        }
        return render(request, 'products/product.html', context)
