from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def resume(request):
    return render(request, 'resume.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')
