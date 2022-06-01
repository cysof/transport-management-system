from django import forms
from django.forms import ModelForm
from route_permit.models import Owner


class OwnerForm(ModelForm):
    
    class Meta:
        model = Owner
        fields = '__all__'
        
    
    def __init__(self, *args, **kwargs):
        super(OwnerForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control-line', 'class': 'form-control'})
