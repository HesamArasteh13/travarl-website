from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponse
def index (request):
    return render (request , 'home_page/index.html')

def about(request):
    return render (request , 'home_page/about.html')

def contact (request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    return render (request , 'home_page/contact.html' , {'form':form})

def test (request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse ('done')
        else :
            print(form.errors)
            return HttpResponse ('invalid input')
    form = ContactForm()
    return render (request , 'test.html', {'form':form})