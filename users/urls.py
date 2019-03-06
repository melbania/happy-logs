"""Defines url patterns for users."""
from django.conf.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'

urlpatterns = [
    # Login page
    # url(r'^login/$', login, {'template_name': 'users/login.html'}, 
        # name='login'),
    path(r'^login$', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    
    # Logout page
    path(r'^logout/$', views.logout_view, name='logout'),

    # Registration page
    path(r'^register/$', views.register, name='register'),
]