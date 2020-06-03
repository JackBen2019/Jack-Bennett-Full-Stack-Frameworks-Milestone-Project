from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils import timezone
from .models import Post, Customer
from checkout.models import Order
from .forms import ForumPostForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from .decorators import unauthenticated_user, allowed_users, admin_only


def about(request):
    """Return the about.html file"""
    return render(request, 'about.html')


"""
Customer view assisted by Dennis Ivy
(https://www.youtube.com/playlist?list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO)
"""

def customer(request, pk):
    """Return the customer.html file"""
    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all()
    order_count = orders.count()

    context = {'customer':customer, 'orders':orders, 'order_count':order_count}
    return render(request, 'customer.html', context)


def customer_no_orders(request):
    """Return the customer_no_orders.html file"""

    user = User.objects.get(email=request.user.email)
    username = User.objects.get(username=request.user.username)
    return render(request, 'customer_no_orders.html', {"profile": user})


"""
Dashboard view assisted by Dennis Ivy
(https://www.youtube.com/playlist?list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO)
"""

def dashboard(request):
    """Return the dashboard.html file"""
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders, 'customers':customers,
    'total_orders':total_orders, 'pending':pending}

    return render(request, 'dashboard.html', context)

@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('about'))


def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('about'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            messages.success(request, "You have successfully logged in!")

            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('about'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('about'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('about'))
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})

@login_required
def user_profile(request):
    """The user's profile page"""
    
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})

@login_required
def get_forum(request):
    """
    Will return a list of posts that were published prior to 'now'
    and render them to the 'forum.html' template
    """

    posts = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "forum.html", {'posts': posts})

@login_required
def forum_post_details(request, pk):
    """
    Create a view that returns a single
    post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is not found
    """

    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    post_creator = post.creator_id
    return render(request, "forum_post_details.html", {'post': post, 'post_creator': post_creator})

@login_required
def create_forum_post(request, pk=None):
    """ Create a view that allows us to create a post """

    post = get_object_or_404(Post, pk=pk) if pk else None
    if not post:
        post = Post.objects.create(creator_id=request.user)
    if request.method == "POST":
        form = ForumPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('forum_post_details', post.pk)
    else:
        form = ForumPostForm(instance=post)
    return render(request, 'forum_post_form.html', {'form': form})

@login_required
def edit_forum_post(request, pk=None):
    """ Create a view that allows us to edit a post """
    post = get_object_or_404(Post, pk=pk)
    if request.user.id != post.creator_id:
        messages.error(request, 'You are unable to edit this post')
        return redirect('get_forum')

    if request.method == "POST":
        edit_post = ForumPostForm(request.POST, request.FILES, instance=post)
        if edit_post.is_valid():
            edit_post.save()
            messages.success(request,
            'You have successfully updated your post')
            return redirect('forum_post_details', post_id)

            edit_post = CreatePost(instance=post)

            return render(request, 'forum_post_form.html', {'form': edit_post, 'post': post})
