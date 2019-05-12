from django.conf import path
from . import views

urlpatterns = patterns(
        path('/add',views.add, name = 'add'),
        path('/remove',views.remove, name = 'remove'),
        path('/show',views.show, name = 'show'),
)

