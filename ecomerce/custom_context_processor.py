from product.models import Categories


def category_renderer(request):
    return {
        'all_categories': Categories.objects.all(),
        'count_all_categories': Categories.objects.count(),
    }
