from django.urls import path
from .import views

app_name = 'add_owner'

urlpatterns = [
    path('', views.index, name='index'),
]
