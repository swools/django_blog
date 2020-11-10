from django.shortcuts import render
from .models import Post
# Create your views here.


def index(request):
    """The home page for Blogs"""
    posts = Post.objects.order_by('created_on')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)
