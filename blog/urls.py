from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path ('' , index , name='index'),
    path ('single/' , single , name='single'),
    path ('<slug:test>' , test , name='test')
]