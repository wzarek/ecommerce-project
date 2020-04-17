from django.shortcuts import render
from .models import Product
from django.http import Http404

def home(request):
    template = 'shop/index.html'
    context = {'product' : Product.objects.all()}
    return render(request, template, context)

def singleprod(request, slug):
    try:
        product = Product.objects.get(slug = slug)
        template = 'shop/single.html'
        context = {
            'product' : product,
            'products': Product.objects.all()
        }
        return render(request, template, context)
    except:
        raise Http404

