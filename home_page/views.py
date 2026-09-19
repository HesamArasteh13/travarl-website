from django.shortcuts import render
from home_page.models import Contact

def index (request):
    return render (request , 'home_page/index.html')

def about(request):
    return render (request , 'home_page/about.html')

def contact (request):
    return render (request , 'home_page/contact.html')

def test (request):
    if request.method == 'POST':
         name = request.POST.get('name')
         email = request.POST.get('email')
         message = request.POST.get('message')
         subject = request.POST.get('subject')
         c = Contact()
         c.name = name
         c.email = email
         c.message = message 
         c.subject = subject
         c.save()
    return render (request , 'test.html')