from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserRegistration,UploadFileForm
from django.contrib.auth.decorators import login_required
from .models import Profile


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

@login_required
def show_user_profile(request):
    return render(request,'user/profile.html',{'title':'профиль пользователя',})


@login_required
def change_user_information(request):
    if request == "POST":
        form = UploadfileForm(request.POST,request.FILES)
        if form.is_valid():
            m = user.objects.get(pk = course_id)
            m.model_pic = form.cleaned_data['image']
            m.save()
            return HttpResponse('upload image success')
    return render(request,'user/change_form.html',{'title':'change user information'})


