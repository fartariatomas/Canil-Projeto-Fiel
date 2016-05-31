from django.views import generic
from .models import Dog


class IndexView(generic.ListView):
    template_name = 'dogs/index.html'
    context_object_name = 'all_dogs'

    def get_queryset(self):
        list_dogs = Dog.objects.all()
        if len(list_dogs)%2!=0:
            list_dogs.append(None)
        list_dogs_in_pairs = [[list_dogs[x],list_dogs[x+1]] for x in range(0,len(list_dogs),2)]
        return list_dogs_in_pairs


class DetailView(generic.DetailView):
    model = Dog
    template_name = "dogs/detail.html"
