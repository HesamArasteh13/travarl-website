from django.shortcuts import render

def login_views(request):
    return render (request , 'accounts/login.html')

# def logout_views(request):
#     return 

def signup_views(request):
    return render (request , 'accounts/signup.html')
