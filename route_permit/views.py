from urllib import request
from django.shortcuts import render
from .models import VehicleDetail
from contact_us .forms import ContactForm
from django .core.mail import send_mail



def index(request):
    vehicles = VehicleDetail.objects.all()
    context = {'vehcile_details':vehicles}
    return render(request, 'route_permit/index.html', context)