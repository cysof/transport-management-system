
from django.contrib import admin
from django.urls import path, include

app_name = 'contact_us'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('contact_us.urls', namespace='contact_us')),
    path('', include('route_permit.urls', namespace='route_permit')),
]