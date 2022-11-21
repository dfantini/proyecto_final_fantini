
from django.shortcuts import redirect, render

#import my models and forms
from smbapp.models import *
from smbapp.forms import *

# Create your views here.
def smbapp_home (request):
    return render (request, 'smbapp/index.htm')