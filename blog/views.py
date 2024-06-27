from django.shortcuts import render

def home(request):
    return render(request, template_name: 'home.html')


def login(request):
    return render(request, template_name: 'login.html')

def login(request):
    return render(request, template_name: 'register.html')