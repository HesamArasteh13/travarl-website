from django.shortcuts import render
from home_page.models import Contact
from home_page.forms import NameFor
from django.http import HttpResponse

def index (request):
    return render (request , 'home_page/index.html')

def about(request):
    return render (request , 'home_page/about.html')

def contact (request):
    return render (request , 'home_page/contact.html')

def test (request):
    if request.method == 'POST':
        # name = request.POST.get('name')
        # print (name)
        form = NameFor(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            c = Contact()
            c.name = name
            c.email = email
            c.subject = subject
            c.message = message
            c.save()
            return HttpResponse ('O.K')
        else :
            return HttpResponse ('not O.K')

    form = NameFor()
    return render (request , 'test.html' , {'form':form})