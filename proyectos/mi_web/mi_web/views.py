from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def top(request):
    return render(request, 'top.html', {})

def otros(request):
    return render(request, 'otros.html', {})