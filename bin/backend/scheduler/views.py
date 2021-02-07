from django.shortcuts import render
from .models import Criteria
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def criteria(request):
    return render(request, 'scheduler/index.html')



# Create your views here.
class PostListView(ListView):
    model = Criteria
    # content = {'criterias': Criteria.objects.all()}
    context_object_name = 'criterias'
    template_name = 'scheduler/test.html'

class PostCreateView(CreateView):
    model = Criteria
    # content = {'criterias': Criteria.objects.all()}
    fields = ['RotationType', 'TypeAmount']