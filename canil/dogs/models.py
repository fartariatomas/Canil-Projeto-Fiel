from django.db import models
from image_cropping import ImageRatioField
from django.core.urlresolvers import reverse


class Dog(models.Model):
    name = models.CharField(max_length=100)
    colors = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=10, choices=(
        ('M', 'Macho'), ('F', 'Fêmea')))
    day_in = models.DateField()

    def get_absolute_url(self):
        return reverse('dogs:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Photo(models.Model):
    album_name = models.ForeignKey(Dog, on_delete=models.CASCADE)
    image_file = models.ImageField(blank=True, null=True)
    cropping = ImageRatioField('image_file', '430x360')

    def __str__(self):
        return self.album_name.name
