from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductPostForm


def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def product_details(request, pk):
    """
    Create a view that returns a single
    post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is not found
    """

    products = get_object_or_404(Product, pk=pk)
    products.save()
    return render(request, "productdetails.html", {"products": products})

def edit_product(request, pk):
    """ 
    Edit a single product 
    """
    products = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductPostForm(request.POST, instance=products)
        if form.is_valid():
            product = form.save()
            return redirect(product_details, product.pk)
    else:
        form = ProductPostForm(instance=products)
    return render(request, 'editproduct.html', {"form": form})

def add_product(request, pk=None):
    """
    Add a single product
    """

    products = get_object_or_404(Product, pk=pk) if pk else None
    if request.method == "POST":
        form = ProductPostForm(request.POST, request.FILES, instance=products)
        if form.is_valid():
            product = form.save()
            return redirect(product_details, product.pk)
    else:
        form = ProductPostForm(instance=products)
    return render(request, 'addproductform.html', {"form": form})