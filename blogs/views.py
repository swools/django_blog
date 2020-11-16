from django.shortcuts import render
from .models import Post
from django.db.models.functions import Extract
from datetime import datetime
# Create your views here.


def index(request):
    """The home page for Blogs"""
    posts = Post.objects.order_by('-created_on')
    context = {'posts': posts}

    return render(request, 'blogs/index.html', context)


def post(request, post_id):
    """Show a single post page"""
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'blogs/post.html', context)


def family(request):
    """Page for all blog posts in Family category"""
    family_posts = Post.objects.filter(
        category='FAMILY').order_by('-created_on')
    context = {'family_posts': family_posts}

    return render(request, 'blogs/family.html', context)


def garden(request):
    """Page for all blog posts in Garden category"""
    garden_posts = Post.objects.filter(
        category='GARDEN').order_by('-created_on')
    context = {'garden_posts': garden_posts}

    return render(request, 'blogs/garden.html', context)


def cooking(request):
    """Page for all blog posts in Cooking category"""
    cooking_posts = Post.objects.filter(
        category='COOKING').order_by('-created_on')
    context = {'cooking_posts': cooking_posts}

    return render(request, 'blogs/cooking.html', context)
