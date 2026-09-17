from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path ('' , index , name='index'),
    path ('<slug:test>' , single , name='single'),
    path ('category/<str:cat_name>' , blog_category , name='category'),
    path ('test/' , test , name='test'),
]