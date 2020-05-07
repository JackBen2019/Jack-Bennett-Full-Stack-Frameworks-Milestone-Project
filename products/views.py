from django.shortcuts import render
from .models import Product


def all_products(request):
    products = Products.objects.all()
    return render(request, "products.html", {"products": products})