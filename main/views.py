from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import RecordForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count

def index(request):
    product = Products.objects.all()
    streamrecord = Stream.objects.all()
    
    popular_products = Products.objects.filter().order_by('-likes')[:2]
    context = {
        'product': product,
        'popular_products': popular_products,
        'streamrecord': streamrecord,
    }
    return render(request, 'main/index.html', context)

def like_product(request, product_id):
    product = get_object_or_404(Products, id=product_id)

    if request.user.is_authenticated:
        like, created = Like.objects.get_or_create(user=request.user, product=product)
        
        if created: 
            product.likes += 1
        else:
            like.delete()
            product.likes -= 1

        product.save()

    return redirect('index')



def about(request):
    return render(request, 'main/about.html')

def contact(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user if request.user.is_authenticated else None
            feedback.save()
    else:
        form = RecordForm()
        
    return render(request, 'main/contact.html', {'form': form})


