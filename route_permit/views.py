from urllib import request
from django.shortcuts import render
from .models import VehicleDetail
from contact_us .forms import ContactForm
from django .core.mail import send_mail



def index(request):
    data = VehicleDetail.objects.all()
    context = {'datafromdatabase':data}
    return render(request, 'index.html', context)