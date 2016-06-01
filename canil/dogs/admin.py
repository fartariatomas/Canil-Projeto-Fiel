from django.contrib import admin
from .models import Dog, Photo
from image_cropping import ImageCroppingMixin

class DogAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(Dog, DogAdmin)
admin.site.register(Photo)
