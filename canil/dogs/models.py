from django.db import models
from django.core.urlresolvers import reverse


class Dog(models.Model):
    name = models.CharField(max_length=100)
    number_register = models.CharField(max_length=10)
    race = models.CharField(max_length=30, null=True, blank=True)
    mixed_race = models.BooleanField()
    sex = models.CharField(max_length=10, choices=(
        ('Macho', 'Macho'), ('Femea', 'Femea')))
    colour = models.CharField(max_length=100, null=True, blank=True)
    hair = models.CharField(max_length=100, null=True, blank=True)
    tail = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(max_length=20, choices=(
        ('Pequeno Porte', 'Pequeno Porte'), ('Medio Porte', 'Medio Porte'), ('Grande Porte', 'Grande Porte'), ('Muito Grande Porte', 'Muito Grande Porte')))
    profile_pic = models.FileField(upload_to='', blank=True)
    #age = models.IntegerField()
    #day_in = models.DateField()

    def get_absolute_url(self):
        return reverse('dogs:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Photo(models.Model):
    album_name = models.ForeignKey(Dog, on_delete=models.CASCADE)
    photo_img = models.ImageField(upload_to='', null=True, blank=True)
    label = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.album_name.name
