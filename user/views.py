from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserRegistration,UploadFileForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from shop.settings  import SOCIAL_AUTH_FACEBOOK_OAUTH2_KEY, SOCIAL_AUTH_FACEBOOK_OAUTH2_SECRET





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
    return render(request,'user/registration.html',{'form':form ,'title':'регистрация пользователя','key':SOCIAL_AUTH_FACEBOOK_OAUTH2_KEY,'secret':SOCIAL_AUTH_FACEBOOK_OAUTH2_SECRET})

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


