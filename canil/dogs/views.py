from django.views import generic
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from .models import Dog, Photo


class IndexView(generic.ListView):
    template_name = 'dogs/index.html'
    context_object_name = 'all_dogs'

    def get_queryset(self):
        return Dog.objects.all()


class DetailView(generic.DetailView):
    model = Dog
    template_name = "dogs/detail.html"

class PhotoCreate(generic.CreateView):
    model = Photo
    fields = ['album_name', 'photo_img', 'label']
    success_url = reverse_lazy('dogs:index')