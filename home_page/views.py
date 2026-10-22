from django.shortcuts import render
from .forms import ContactForm , NewsletterForm
from django.http import HttpResponse , HttpResponseRedirect
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


def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/')

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