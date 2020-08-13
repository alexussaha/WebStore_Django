"""
Definition of urls for WebStore_Django.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^', include('products.urls')),
    url(r'^', include('app.urls')),
    url(r'^', include('orders.urls')),
    path('admin/', admin.site.urls),
] 