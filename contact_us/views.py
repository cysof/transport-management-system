from email import message
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail



def contactform(request):
    if request.method == 'GET':
        form = ContactForm()
    
    else:
        
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
    
    #send mail.
            send_mail(
                subject,
                email,
                message,
                ['cp4reallife@yahoo.com']
            )
             
    return render(request, 'contact.html', {'form': form})
