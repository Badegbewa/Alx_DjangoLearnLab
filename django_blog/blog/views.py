from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from .forms import RegistrationForm, ProfileForm
from .models import Post
from django.contrib.auth.views import LogoutView

def home(request):
    return render(request, 'blog/base.html')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def register_view(request):
    """
    GET  -> show empty sign-up form
    POST -> validate & create user, then log them in and redirect to profile
    """
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            messages.success(request, "Welcome! Your account was created.")
            return redirect("profile")
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = RegistrationForm()
    return render(request, "auth/register.html", {"form": form})


@login_required
def profile_view(request):
    """
    GET  -> show a form pre-filled with the current user's info
    POST -> validate & save changes to the current user
    """
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "auth/profile.html", {"form": form})