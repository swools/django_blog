"""Defines URL patterns for blogs."""
from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('family/', views.family, name='family'),
    path('garden/', views.garden, name='garden'),
    path('cooking/', views.cooking, name='cooking'),
    # Detail page for single post
    path('posts/<int:post_id>/', views.post, name="post")
]
