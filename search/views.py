from django.shortcuts import render
from products.models import Product
from accounts.models import Post

def do_search_product(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})

def do_search_review(request):
    posts = Post.objects.filter(title__icontains=request.GET['q'])
    return render(request, "reviews.html", {'posts': posts})