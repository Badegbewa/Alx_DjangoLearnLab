from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, register_view, profile_view
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('posts/', views.post_list, name='posts'),

    path('login/',  auth_views.LoginView.as_view(template_name="auth/login.html"),   name='login'),
    path('logout/', auth_views.LogoutView.as_view(),                                 name='logout'),

    path('register/', register_view, name='register'),
    path('profile/',  profile_view,  name='profile'),
]
