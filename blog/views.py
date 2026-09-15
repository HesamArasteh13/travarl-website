from django.shortcuts import render , get_object_or_404
from .models import Post

def index(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render (request , 'blog/blog-home.html', context)

def single(request , test):
    posts = get_object_or_404(Post , id = test)
    context = {'posts':posts}
    return render (request , 'blog/blog-single.html' , context)

