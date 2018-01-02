from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class List(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pass


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default='', on_delete=models.CASCADE)
    pass
