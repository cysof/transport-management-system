from django.urls import reverse
from django.db import models


GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('N', 'Manwoman')
)
class Owner(models.Model):
    National_ID =models.CharField(max_length=11, primary_key=True, verbose_name='National ID care Numner')
    full_name = models.CharField(max_length=150, verbose_name='Full Name of the owner')
    phone_number = models.CharField(max_length=11)
    gender = models.CharField(max_length=7, choices=GENDER)
    citizen_of = models.CharField(max_length=5, verbose_name='selete conutry')
    address_of_owner = models.CharField(max_length=100, verbose_name='address of the owner')
    

    class Meta:
        verbose_name = ("vehicle owner")
        verbose_name_plural = ("Owner Information")

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse("Owner_detail", kwargs={"pk": self.pk})


class VehicleDetail(models.Model):
    vehicle_number = models.CharField(max_length=30, primary_key=True, verbose_name='vehicle number')
    owner = models.ForeignKey(Owner, on_delete=models.PROTECT, verbose_name='owner name')
    model_number = models.CharField(max_length=30, verbose_name='vehicle model number')
    chasis_number = models.CharField(max_length=30, verbose_name='verhicle chasis number')
    engine_number = models.CharField(max_length=30, verbose_name='vehicle engine number')
    vehicle_type = models.CharField(max_length=100, verbose_name='type of vehicle')
    
    
    def __str__(self):
        return self.vehicle_type