from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
app_name = "wind_cart"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.show_home_page,name = "home"),
    path('products/',include('products.urls')),
    path('user/',include('user.urls')),
    url('cart/', include('wind_cart.urls')),



]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

