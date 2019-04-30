from django.shortcuts import render



def show_product_list(request,category_slug = None):
    category = None
    categories = Category.objects.all()
    products = Products.objects.filter(availiable = True)
    if category_slug:
        category = get_object_404(Category,slug = category_slug)
        products = products.filter(category = category)
    return render(request,'templates/products/list.html',{'category':category,
                                                            'categories':categories,
                                                            'products':products})

def priticilar_product(request,id,slug):
    product = get_object_404(Products,id = id ,slug = slug,availiable = True)
    cart_product_form = CartAddProductFrom()
    return render(request,'templates/products/product.html',{'product':product,
                                                             'cart_product_from':cart_product_from})


