from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Product, ProductCategory
from django.http import Http404
from django.db.models import Q

def updateproduct(products):
    for p in products:
        p.inStock = 0
        for i in p.productsize_set.all():
            p.inStock += i.sizeInStock
    return products

def home(request):
    template = 'shop/index.html'
    products = Product.objects.all()
    updateproduct(products)
    context = {'product' : products}
    return render(request, template, context)

def search(request):
    try:
        search = request.GET['search']
    except:
        search = None
    if search:
        products = Product.objects.filter(Q(brand__icontains=search) | Q(model__icontains=search))
        updateproduct(products)
    else:
        products = None
    template = 'shop/search.html'
    context = {'query': search, 'products': products}
    return render(request, template, context)

def subcategory(request, cat, subcat):
    try:
        products = ProductCategory.objects.filter(title=subcat).get(parent__title=cat).product_set.all()
    except:
        products = None
    subcategories = ProductCategory.objects.filter(parent__title=cat)
    template = 'shop/category.html'
    context = {'products':products, 'cat': cat, 'subcat':subcat, 'subcats': subcategories}
    return render(request, template, context)

def category(request, cat):
    try:
        products = ProductCategory.objects.select_related().get(title=cat).product_set.all()
        updateproduct(products)
    except:
        products = None
    subcategories = ProductCategory.objects.filter(parent__title=cat)
    template = 'shop/category.html'
    context = {'products':products, 'cat': cat, 'subcats': subcategories}
    return render(request, template, context)

def subcatprod(request, cat, subcat, slug):
    try:
        product = Product.objects.get(slug = slug)
        products = Product.objects.all()
        updateproduct(products)
        if product.categories.all()[0].title in cat or product.categories.all()[0].title in subcat:
            template = 'shop/single.html'
            context = {
                'product' : product,
                'products': products,
                'cat': cat,
                'subcat': subcat
            }
            return render(request, template, context)
        else:
            raise Http404
    except:
        raise Http404

def singleprod(request, slug):
    try:
        product = Product.objects.get(slug = slug)
        cat = product.categories.all()[0]
        subcat = product.categories.all()[1]
        # template = 'shop/single.html'
        # context = {
        #     'product': product,
        #     'products': Product.objects.all()
        # }
        # return render(request, template, context)
        return HttpResponseRedirect(reverse('subcatprod', kwargs={'cat':cat, 'subcat':subcat, 'slug':slug}))
    except:
        raise Http404

