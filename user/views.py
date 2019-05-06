from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def show_user_profile(request):
    return render(request,'user/profile.html')

def show_current_bought(request):
    pass
def register(request):
    if request.method =='POST':
        if form.is_valid():
            form.save()
            username =  request.POST.get('username')
            messages.success(request,f'Аккаунт  {username} был успешно создан')
            return redirect('user_page')

    form = UserCreationForm()
    return render(request,'user/registration.html',{'title':'регистрация нового пользователя',
                                                    'form':form })
