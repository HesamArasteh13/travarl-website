from django.shortcuts import render

# Create your views here.

def index (request):
    return render (request , 'home_page/index.html')

def about(request):
    return render (request , 'home_page/about.html')

def contact (request):
    return render (request , 'home_page/contact.html')

def test (request):
    if request.method == 'POST':
        print (request.POST.get('name'))
    return render (request , 'test.html')