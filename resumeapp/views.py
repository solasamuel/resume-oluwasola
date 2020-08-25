from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse("Hello, world. You're at the home page.")


def resume(request):
    return HttpResponse("Hello, world. You're at the resume page.")


def blog(request):
    return HttpResponse("Hello, world. You're at the blog page.")


def contact(request):
    return HttpResponse("Hello, world. You're at the contact page.")
