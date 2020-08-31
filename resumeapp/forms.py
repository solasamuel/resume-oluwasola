from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(label='Subject', required=True)
    sender = forms.EmailField(label='Your email', required=True)
    message = forms.CharField(label='Your message', widget=forms.Textarea, required=True)