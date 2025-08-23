from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def home(request):
    return render(request, 'blog/base.html')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('posts')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
