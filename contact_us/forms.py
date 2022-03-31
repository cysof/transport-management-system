import email
from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)