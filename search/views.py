from django.shortcuts import render
from products.models import Product


def do_search_product(request):
    """
    Allows the user to search for a product
    on the 'Services' page
    """

    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, 'products.html', {'products': products})
