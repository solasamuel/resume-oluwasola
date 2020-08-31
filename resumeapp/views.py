from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def resume(request):
    return render(request, 'resume.html')


def blog(request):
    return render(request, 'blog.html')

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, sender, ['oluwasolasamuel4@gmail.com'], fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success_page')
    return render(request, "contact.html", {'form': form})

def success(request):
    return render(request, 'success.html')
