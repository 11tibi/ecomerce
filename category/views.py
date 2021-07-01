from django.shortcuts import render

# Create your views here.


def categories(request):
    context = {}
    return render(request, 'category/categories.html', context)
