from django.shortcuts import render
from django.views import View

# Create your views here.


class Product(View):
    def get(self, request):
        context = {}
        return render(request, 'products/products.html', context)

    def post(self, request):
        pass