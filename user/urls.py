"""shop URL Confim``gurgtion

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_view



urlpatterns = [
    path('profile/',views.show_user_profile,name = 'profile'),
    path(r'^profile/?P<username>/?<current_bought>/',views.show_current_bought,name = 'bought'),
    path('reg/',views.register,name = 'reg'),
    path('user',views.register,name = 'auth'),
    path('login',auth_view.LoginView.as_view(template_name = 'user/user.html'),name = 'login'),
    path('exit',auth_view.LogoutView.as_view(template_name = 'user/exit.html'),name = 'exit'),
]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
