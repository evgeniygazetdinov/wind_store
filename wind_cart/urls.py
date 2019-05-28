from django.urls import path
from  . import views

urlpatterns = [
    path('add/<?P<product_id>',views.CartAdd,name = 'cart_add'),
    path('remove/<?P<product_id>',views.CartRemove,name = 'delete_from_cart'),
    path('show/',views.CartDetail,name = 'show_cart_items'),
]


