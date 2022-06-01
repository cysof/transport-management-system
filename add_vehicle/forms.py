from dataclasses import field
from pyexpat import model
from django import forms
from django.forms import ModelForm, widgets
from route_permit.models import VehicleDetail


class VeihcleForm(ModelForm):
    
    class Meta:
        model = VehicleDetail
        fields = '__all__'
        
    
    def __init__(self, *args, **kwargs):
        super(VeihcleForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control-line', 'class': 'form-control'})
