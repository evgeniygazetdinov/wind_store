from django.contrib import admin
from .models import Luggage,Category



class Category_Admin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,Category_Admin)

class Luggage_Admin(admin.ModelAdmin):
    list_display = ['name','slug','category','price','stock','available','created','updated']
    list_filter = ['available','created','updated','category' ]
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Luggage,Luggage_Admin)

