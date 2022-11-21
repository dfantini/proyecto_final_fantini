from django.urls import path
from smbapp import views

urlpatterns = [
   path ( '', views.smbapp_home , name = 'smbapp-home'),
    
]