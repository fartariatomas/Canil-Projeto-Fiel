from django.db import models
from django.core.urlresolvers import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Dog(models.Model):
    name = models.CharField(max_length=100)
    number_register = models.CharField(max_length=10)
    race = models.CharField(max_length=30)
    mixed_race = models.BooleanField()
    sex = models.CharField(max_length=10, choices=(
        ('M', 'Macho'), ('F', 'Fêmea')))
    colour = models.CharField(max_length=100, null=True, blank=True)
    hair = models.CharField(max_length=100, null=True, blank=True)
    tail = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(max_length=20, choices=(
        ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large'), ('extra large', 'Very Large')))
    #age = models.IntegerField()
    #day_in = models.DateField()

    def get_absolute_url(self):
        return reverse('dogs:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Photo(models.Model):
    album_name = models.ForeignKey(Dog, on_delete=models.CASCADE)
    photo_img = models.ImageField(null=True, blank=True)
    photo_img_thumbnail = ImageSpecField(source='photo_img',
                                         processors=[ResizeToFill(400, 300)],
                                         format='JPEG',
                                         options={'quality': 60})

    def __str__(self):
        return self.album_name.name
