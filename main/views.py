from django.shortcuts import render
from .models import *
from .forms import RecordForm

def index(request):
    product = Products.objects.all()
    return render(request, 'main/index.html', {'product': product})

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RecordForm()
        
    return render(request, 'main/contact.html', {'form': form})
