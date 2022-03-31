from django .urls import path
from .import views

app_name = 'route_permit'

urlpatterns = [
    path('', views.index, name='home'),
]