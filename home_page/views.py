from django.shortcuts import render


def index (request):
    return render (request , 'home_page/index.html')

def about(request):
    return render (request , 'home_page/about.html')

def contact (request):
    return render (request , 'home_page/contact.html')