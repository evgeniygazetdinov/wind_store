from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Luggage as Product
from .wind_cart import Cart
from .forms import CartAddProductForm


@require_POST
def CartAdd(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,id = product_id)
    #this form it's interpritation models with 2-entry which take only requered-post-request
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product = product, quantity = cd['quantity'],
                 update_quantity = cd['update'])
    return redirect('show_cart_items')

def CartRemove(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,id = product_id)
    cart.remove(product)
    return redirect('show_cart_items')

def CartDetail(request):
    art = Cart(request)
    for item in art:
        item['update_quantity_form'] = CartAddProductForm(
                                        initial = {
                                            'quantity':item['quantity'],
                                            'update':True
                                        })
    return render(request,'wind_cart/detail.html',{'art':art})



