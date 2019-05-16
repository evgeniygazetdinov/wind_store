from django.shortcuts import render
from django.http import HttpResponse

from .carton.cart import Cart
import sys
sys.path.append("..")

from products.models  import Luggage as Product


def return_cart_items():
    pass



def add(request):
    cart = Cart(request.session)
    product = Product.object.get(id = request.GET.get('id'))
    cart.add(product,price = product.price)
    HttpResponse('add')


def remove(request):
    cart = Cart(request.session)
    product = Product.object.get(id = request.Get.get('id'))
    cart.remove(product)
    return HttpResponse('del')


def show(request):
    return render(request,'goods_trolley/basket.html')
