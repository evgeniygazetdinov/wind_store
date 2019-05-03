from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import Category
from .models import Luggage as Products


def show_product_list(request,category_slug = None):
    category = None
    categories = Category.objects.all()
    products = Products.objects.filter(available = True)
    if category_slug:
        category = get_object_404(Category,slug = category_slug)
        products = products.filter(category = category)
    return render(request,'products/list.html',{'title': 'список товаров',
                                                            'category':category,
                                                            'categories':categories,
                                                            'products':products})

def priticilar_product(request,id,slug):
    product = get_object_or_404(Products,id = id ,slug = slug,available = True)
    return render(request,'products/product.html',{'product':product})

def check(request):
    return HttpResponse("return this string")

def base_page(request):
    return HttpResponse("base string")
