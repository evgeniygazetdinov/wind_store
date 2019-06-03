from django.shortcuts import render
import os


def return_weather():
    from .pa import gatchina_weather
    return gatchina_weather()




def show_home_page(request):
    path = os.getcwd()
    with open(path+'/shop/small.txt','r') as text:
        n = text.read()
        print(n)
        text.close()
        if request.method == "POST":
            ans = request.POST.dict()
            for a in ans.keys():
                print(a)
            print(ans)
            print(((request.session.items())))
            print('this is from post')
            request.session['hui_moi'] = 'blue'
            print(((request.session.items())))
    return render(request,'shop/base.html',{'name':'scientia est potentia','n':n})
