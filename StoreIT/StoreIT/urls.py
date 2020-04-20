"""
Definition of urls for StoreIT.
"""

from datetime import datetime
from django.urls import path, include, re_path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from Storage import urls


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    re_path(r'^accounts/', include('allauth.urls')),
    re_path('storage/', include('Storage.urls')),
]
