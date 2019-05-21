from django.shortcuts import render,HttpResponse,get_object_or_404,get_list_or_404,render_to_response
from .models import Category
from .models import Luggage as Products
from django.template import RequestContext
from django.contrib import messages



def show_product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Products.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'products/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })


def priticilar_product(request,id,slug):
    product = get_object_or_404(Products,id = id ,slug = slug,available = True)
    return render(request,'products/product.html',{'product':product})

