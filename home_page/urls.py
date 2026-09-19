from django.urls import path
from .views import *

app_name = 'home_page'

urlpatterns = [
    path('', index , name='index'),
    path('about/', about , name='about'),
    path('contact/', contact , name='contact'),
    path('test/', test , name='test'),
]