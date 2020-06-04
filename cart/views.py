from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Cart, CartItem
from shop.models import Product

def cart(request):
    try:
        nowID = request.session['cartID']
    except:
        nowID = None
    if nowID:
        cart = Cart.objects.get(id=nowID)
        context = {'cart': cart, 'products': Product.objects.all()}
        totalPrice = 0.00
        for i in cart.cartitem_set.all():
            if i.product.sale != None:
                iPrice = float(i.product.sale) * i.quantity
                totalPrice += iPrice
            else:
                iPrice = float(i.product.price) * i.quantity
                totalPrice += iPrice
        cart.total = totalPrice
        cart.save()
        request.session['itemsInCart'] = cart.cartitem_set.all().count()
    else:
        context = {'cartEmpty': True, 'products': Product.objects.all()}
    template = 'cart/cartview.html'
    return render(request, template, context)

def updateCart(request, slug, quantity):
    request.session.set_expiry(259200) #3 dni
    try:
        nowID = request.session['cartID']
    except:
        newCart = Cart()
        newCart.save()
        request.session['cartID'] = newCart.id
        nowID = newCart.id
    cart = Cart.objects.get(id=nowID)
    product = Product.objects.get(slug=slug)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if int(quantity)==0:
        cart_item.delete()
    else:
        cart_item.quantity = quantity
        cart_item.save()
    # if not cart_item in cart.items.all():
    #     cart.items.add(cart_item)
    # else:
    #     cart.items.remove(cart_item)
    return HttpResponseRedirect(reverse('cart'))
