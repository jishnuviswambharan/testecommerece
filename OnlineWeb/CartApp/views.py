from django.shortcuts import get_object_or_404, redirect, render
from .models import Cart, CartItem
from OnlineApp.models import Product
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

# create card ID 

def _cart_id(request):
    cart  = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


# item add to cart function
def add_cart(request,product_id):
    #feching product id
    product=Product.objects.get(id=product_id)
    
    try:
        # feching cart id
        cart = Cart.objects.get(cart_id = _cart_id(request))
    except Cart.DoesNotExist:
        #if cart id is not exis create the same
        cart  =Cart.objects.create(cart_id = _cart_id(request))
        cart.save(),

    try:
        #feching cart item 
        cart_item  =CartItem.objects.get(product = product, cart = cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity +=1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product, quantity = 1,cart = cart )
        # cart_item.quantity = 1
        cart_item.save()
    return redirect ('CartApp:cartdetail')

def cartdetail(request,total = 0, counter = 0, cart_items = None):
    try:
        cart = Cart.objects.get(cart_id = _cart_id (request))
        cart_items = CartItem.objects.filter(cart = cart, active = True)
        for cart_item in cart_items:
            total+=(cart_item.product.price * cart_item.quantity)
            counter+=cart_item.quantity
    except ObjectDoesNotExist:
        pass
    # dict = (cart_item = cart_item, total = total, counter = counter)
    return render (request, 'cart.html', dict(cart_items=cart_items,total=total,counter=counter))


#cart Delete Function

def cart_delete(request, product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404 ( Product, id = product_id)
    cart_item = CartItem.objects.get(cart = cart, product = product)
    if cart_item.quantity > 1 :
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect ('CartApp:cartdetail')


#delete all items from Cart by using trash simbol
def cart_remove(request, product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404 ( Product, id = product_id)
    cart_item = CartItem.objects.get(cart = cart, product = product)
    cart_item.delete()
    # cart_item.save()
    return redirect ('CartApp:cartdetail')


def delivery(request):
    return render(request,'address.html')





