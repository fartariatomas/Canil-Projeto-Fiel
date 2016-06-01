from django.views import generic
from .models import Dog


class IndexView(generic.ListView):
    template_name = 'dogs/index.html'
    context_object_name = 'all_dogs'

    def get_queryset(self):
        return Dog.objects.all()


class DetailView(generic.DetailView):
    model = Dog
    template_name = "dogs/detail.html"
