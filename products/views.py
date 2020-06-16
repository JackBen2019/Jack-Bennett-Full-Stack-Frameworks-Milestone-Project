from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductPostForm


@login_required
def all_products(request):
    """Returns the 'Services' page"""

    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


@login_required
def product_details(request, pk):
    """
    Create a view that returns a single
    post object based on the post ID (pk) and
    render it to the 'productdetails.html' template.
    Or return a 404 error if the product is not found
    """

    products = get_object_or_404(Product, pk=pk)
    product_creator = products.prod_creator_id
    return render(request, 'productdetails.html',
                  {'products': products, 'pk': pk,
                   'product_creator': product_creator})


@login_required
def edit_product(request, pk):
    """Edit a single product"""

    products = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductPostForm(request.POST, instance=products)
        if form.is_valid():
            product = form.save()
            return redirect(product_details, product.pk)
    else:
        form = ProductPostForm(instance=products)
    return render(request, 'editproduct.html', {'form': form})


@login_required
def add_product(request):
    """Add a single product to the 'Services' page"""

    if request.method == 'POST':
        form = ProductPostForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('product_details', product.id)
    else:
        form = ProductPostForm()
    return render(request, 'addproductform.html', {'form': form})
