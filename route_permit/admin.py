from django.contrib import admin
from route_permit .models import Owner, VehicleDetail

class OwnerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Owner)
admin.site.register(VehicleDetail)