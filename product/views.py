from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.db.models import Avg
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from product.models import Product, Specs, Reviews
from accounts.models import User, ProductBought
from .forms import ReviewForm

# Create your views here.


class Products(View):
    def get(self, request, category):
        return redirect(f'{category}/page1')


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


class ProductPage(View):
    def get(self, request, category, product, product_code):
        prod = Product.objects.select_related('discount', 'category', 'inventory').filter(category__link=category, link=product).all()
        specs = Specs.objects.select_related('prod').filter(prod__link=product).all()
        reviews = Reviews.objects.select_related('user').filter(prod=prod[0].id)
        rating__avg = Reviews.objects.select_related('user').filter(prod=prod[0].id).aggregate(Avg('rating'))['rating__avg']
        review_form = ReviewForm()
        user_review = []
        product_owned = False
        if request.user.is_authenticated:
            try:
                product_owned = ProductBought.objects.select_related('user').filter(product=prod[0].id, user=request.user.id).exists()
                user_review = Reviews.objects.select_related('user').filter(prod=prod[0].id, user=request.user.id)[0]
            except IndexError:
                user_review = []

        context = {
            'product': prod[0],
            'specs': specs,
            'reviews': reviews,
            'review_form': review_form,
            'rating__avg': rating__avg,
            'user_review': user_review,
            'product_owned': product_owned,
        }
        return render(request, 'products/product.html', context)


class AddReview(View):
    def post(self, request, product):
        product_id = ProductBought.objects.select_related('product', 'user').\
            filter(product__link=product, user__id=request.user.id).values('product__id')

        if product_id.count() == 1:
            review_exists = Reviews.objects.select_related('prod', 'user').\
                filter(prod__link=product, user__id=request.user.id).values('id')

            form = ReviewForm(request.POST)
            if form.is_valid():
                if review_exists.exists():
                    obj = Reviews.objects.get(id=review_exists[0]['id'])
                    obj.rating = form.cleaned_data["stars"]
                    obj.description = form.cleaned_data["text_review"]
                    obj.save()
                else:
                    obj = Reviews()
                    obj.user = request.user.id
                    obj.rating = form.cleaned_data["stars"]
                    obj.description = form.cleaned_data["text_review"]
                    obj.prod = product_id
                    obj.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
