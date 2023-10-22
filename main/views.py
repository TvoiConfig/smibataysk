from django.shortcuts import render
from .models import *
from .forms import RecordForm

def index(request):
    product = Products.objects.all()
    return render(request, 'main/index.html', {'product': product})

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')
