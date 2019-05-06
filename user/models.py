from django.db import models
from django.contrib.auth.models  import User


class Profile(models.Model):
    name = models.OneToOneField(User,on_delete = models.CASCADE)
    image = models.ImageField(default = 'defautl.jpg',upload_to = 'user_img')
    current_bought =  models.BooleanField(default = 0)
    address = models.TextField(default =False)
    date_registration = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return 'файл пользователя {}'.format(self.name)

