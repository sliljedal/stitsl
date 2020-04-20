from django.db import models
from django.contrib.auth.models import User

class Storage(models.Model):
    name        = models.CharField          (max_length = 20)
    city        = models.CharField          (max_length = 20)
    user        = models.ManyToManyField    (User, default = 1,      related_name="+")
class Box(models.Model):
    name        = models.CharField          (max_length=20)
    code        = models.IntegerField       ()
    storage     = models.ForeignKey         (Storage, default = 1,  on_delete = models.SET_DEFAULT, related_name='+')
    user        = models.ManyToManyField    (User, default = 1 ,      related_name="+")

class Item(models.Model):
    name        = models.CharField          (max_length=255)
    description = models.CharField          (max_length=500)
    box         = models.ForeignKey         (Box,   default = 1,      on_delete = models.SET_DEFAULT, related_name='+')
    user        = models.ManyToManyField    (User,  default = 1,        related_name="+")