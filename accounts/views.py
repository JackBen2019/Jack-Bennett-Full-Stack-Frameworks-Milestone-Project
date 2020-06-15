from django.shortcuts import render, redirect, reverse, \
    get_object_or_404
from django.utils import timezone
from .models import Post, Customer
from .forms import ForumPostForm, UserLoginForm, UserRegistrationForm, \
    EditProfileForm, CommentPostForm

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    """Return the index.html file"""

    return render(request, 'index.html')


def privacy_policy(request):
    """Return the privacy_policy.html file"""

    return render(request, 'privacy_policy.html')


def about(request):
    """Return the about.html file"""

    return render(request, 'about.html')


@login_required
def profile(request, pk):
    """
    Return the profile.html file as a the profile page
    if the user had made 0 orders
    """

    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all()
    order_count = orders.count()

    return render(request, 'profile.html', {'customer': customer,
                  'orders': orders, 'order_count': order_count})


@login_required
def profile_no_orders(request):
    """
    Return the profile_no_orders.html file as a the profile page
    if the user has made 1 or more orders
    """

    user = User.objects.get(email=request.user.email)
    username = User.objects.get(username=request.user.username)
    return render(request, 'profile_no_orders.html', {'profile': user})


@login_required
def edit_profile(request):
    """
    A view that gives the user the option to
    update thier account details
    """

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile_no_orders')
    else:
        form = EditProfileForm(instance=request.user)
        return render(request, 'edit_profile.html', {'form': form})


def change_password(request):
    """
    A view that gives the user the option to
    update thier password, seperate from the
    edit_profile page
    """

    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('password_reset_done')
        else:
            return redirect('password_reset')
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'registration/password_reset_form.html',
                      {'form': form})


@login_required
def logout(request):
    """Log the user out"""

    auth.logout(request)
    messages.success(request, 'You have successfully been logged out')
    return redirect(reverse('about'))


def login(request):
    """Return a login page"""

    if request.user.is_authenticated:
        return redirect(reverse('about'))
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                    password=request.POST['password'])
            messages.success(request, 'You have successfully logged in!'
                             )

            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('about'))
            else:
                login_form.add_error(None,
                        'Your username or password is incorrect')
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def registration(request):
    """Return the registration page"""

    if request.user.is_authenticated:
        return redirect(reverse('about'))

    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                    password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request,
                                 'You have successfully registered')
                return redirect(reverse('about'))
            else:
                messages.error(request,
                               'Unable to register your account at this time'
                               )
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html',
                  {'registration_form': registration_form})


@login_required
def get_forum(request):
    """
    Will return a list of posts that have been published
    and render them to the 'forum.html' template
    """

    posts = Post.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-published_date')

    gen_discussion = Post.objects.filter(category='General Discussion')

    events = Post.objects.filter(category='Events')

    return render(request, 'forum.html', {
                  'posts': posts,
                  'events': events,
                  'gen_discussion': gen_discussion})


@login_required
def gen_discussion(request):
    """
    Will return a list of posts that have a category
    that matches 'General Discussion'
    """

    gen_discussion = Post.objects.filter(category='General Discussion')

    return render(request, 'general_discussion.html',
                  {'gen_discussion': gen_discussion})


@login_required
def events(request):
    """
    Will return a list of posts that have a category
    that matches 'Events'
    """

    events = Post.objects.filter(category='Events')

    return render(request, 'events.html', {'events': events})


@login_required
def forum_post_details(request, pk):
    """
    Allows the user to view a posts details based on
    the post ID (pk) and renders it to the
    'forum_post_details.html' template.
    """

    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    post_creator = post.creator_id
    return render(request, 'forum_post_details.html', {'post': post,
                  'post_creator': post_creator})


@login_required
def comment_post_form(request, pk):
    """ A view that allows us to add a comment to a post """

    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentPostForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('forum_post_details', post.pk)
    else:
        form = CommentPostForm()
        return render(request, 'comment_post_form.html', {'form': form})


@login_required
def create_forum_post(request):
    """
    A view that allows us to create a post, which
    will then be added to the forum
    """

    if request.method == 'POST':
        form = ForumPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
        return redirect('forum_post_details', post.id)
    else:
        form = ForumPostForm()
    return render(request, 'forum_post_form.html', {'form': form})


@login_required
def edit_forum_post(request, pk=None):
    """ A view that allows us to edit a post """

    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        edit_post = ForumPostForm(request.POST, request.FILES,
                                  instance=post)
        if edit_post.is_valid():
            edit_post.save()
            messages.success(request,
                             'You have successfully updated your post')
            return redirect('forum_post_details', post.id)

    if request.user != post.creator_id:
        messages.error(request, 'You are unable to edit this post')
        return redirect('get_forum')
    else:
        edit_post = ForumPostForm(instance=post)
        return render(request, 'forum_post_form.html',
                      {'form': edit_post, 'post': post})
