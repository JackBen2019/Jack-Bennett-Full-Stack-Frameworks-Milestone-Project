from django.shortcuts import render
from products.models import Product
from accounts.models import Post

def do_search_product(request):
    """ Allows the user to search for a product """
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})

def do_search_forum(request):
    """ Allows the user to search the forum """`
    posts = Post.objects.filter(title__icontains=request.GET['q'])
    return render(request, "forum.html", {'posts': posts})