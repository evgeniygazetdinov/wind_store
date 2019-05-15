from django.db import models



class CARTO(models.Model):
    date_added = models.DateTimeField(auto_now = True)
    name = models.CharField(max_length = 200,db_index = True)
    quantity = models.PositiveIntegerField()
    username = models.CharField(max_length = 200,db_index = True)

    def user_bought(self):
        return [daw]
