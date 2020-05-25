from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import ForumPostForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm



def index(request):
    """Return the index.html file"""
    return render(request, 'index.html')

def about(request):
    """Return the about.html file"""
    return render(request, 'about.html')

@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))


def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            messages.success(request, "You have successfully logged in!")

            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})


def user_profile(request):
    """The user's profile page"""
    
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})


def get_forum(request):
    """
    Will return a list of posts that were published prior to 'now'
    and render them to the 'forum.html' template
    """

    posts = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "forum.html", {'posts': posts})

def forum_details(request, pk):
    """
    Create a view that returns a single
    post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is not found
    """

    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "forumdetails.html", {'post': post})

def create_or_edit_forum(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending on if the post ID
    is null or not
    """

    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST":
        form = ForumPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(forum_details, post.pk)
    else:
        form = ForumPostForm(instance=post)
    return render(request, 'forumpostform.html', {'form': form})