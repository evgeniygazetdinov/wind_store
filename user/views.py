from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserRegistration

def show_user_profile(request):
    return render(request,'user/profile.html')

def show_current_bought(request):
    pass
def register(request):
    if request.method == "POST":
            form = CustomUserRegistration(request.POST)
            if form.is_valid():
                #take username from your request
                form.save()
                username =  request.POST.get('username')
                messages.success(request,f'Аккаунт  {username} был успешно создан')
                return redirect('home')
    else:
        form = CustomUserRegistration()
    return render(request,'user/registration.html',{'form':form ,'title':'регистрация пользователя'})
