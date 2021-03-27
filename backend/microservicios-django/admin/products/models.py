from django.db import models


# Create your models here.
class Products(models.Model):
    objects = None
    title = models.CharField(max_length=250)
    image = models.CharField(max_length=250)
    likes = models.PositiveIntegerField(default=0)


class User(models.Model):
    objects = None
