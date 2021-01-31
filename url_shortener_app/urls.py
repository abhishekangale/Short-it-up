from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home),
    path('short/', views.shorten),
    path('redirect/<slug:link>/', views.redirect_url),
    path('analytics/', views.get_analytics),
]