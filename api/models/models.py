from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    user_id = models.AutoField
    name = models.CharField(max_length=200)
    contact =models.CharField(max_length=12)
    photo_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updated_at = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self) :
        return self.name
