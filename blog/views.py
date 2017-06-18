from django.shortcuts import render
from django.utils import timezone
from .models import Product
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

def products(request):
    products = Product.objects.all
    return render(request, 'blog/products.html', {'products': products})

def err(request):
    return render(request, 'blog/error.html',)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'blog/product_detail.html', {'product': product})

def homepage(request):
    return render(request, 'blog/base.html', {})

def about(request):
    return render(request, 'blog/about.html', {})
