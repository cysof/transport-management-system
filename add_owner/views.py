from django.shortcuts import render, redirect
from .forms import OwnerForm




def index(request):
    form = OwnerForm()
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('route_permit:home')
    context = {'form': form }
    return render(request, 'add_owner/index.html', context)