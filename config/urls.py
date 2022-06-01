
from django.contrib import admin
from django.urls import path, include

app_name = 'contact_us'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('contact_us.urls', namespace='contact_us')),
    path('', include('route_permit.urls', namespace='route_permit')),
    path('save/', include('add_vehicle.urls', namespace='add_vehicle')),
    path('add_owner/save/', include('add_owner.urls', namespace='add_owner')),
]