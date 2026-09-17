from django import template
from blog.models import Post

register = template.Library()

@register.simple_tag(name='total_posts')
def function ():
    posts = Post.objects.filter(status= 1).count()
    return posts

@register.simple_tag(name='posts')
def function ():
    posts = Post.objects.filter(status=1)
    return posts

@register.filter
def snipets (value , arg=50):
    return value[:arg]+ ' ...'

@register.inclusion_tag('blog/blog-latest.posts.html')
def latestposts ():
    posts = Post.objects.filter(status = 1).order_by('published_date')
    return {'posts':posts}
