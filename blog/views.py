from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render (request , 'blog/blog-home.html', context)

def single(request):
    return render (request , 'blog/blog-single.html')