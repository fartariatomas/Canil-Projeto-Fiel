from django.db import models
from django.core.urlresolvers import reverse


class Dog(models.Model):
    name = models.CharField(max_length=100)
    colors = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    day_in = models.DateField()
    photo = models.FileField()

    def __str__(self):
        return self.name
