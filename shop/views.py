from django.shortcuts import render




def show_home_page(request):
    return render(request,'shop/base.html',{'name':'scientia est potentia'})
