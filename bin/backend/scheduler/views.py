from django.shortcuts import render
from .models import Criteria
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

def criteria(request):
    return render(request, 'scheduler/index.html')



# Create your views here.
class V2ListView(ListView):
    model = Criteria
    # content = {'criterias': Criteria.objects.all()}
    context_object_name = 'criterias'
    template_name = 'scheduler/test.html'

class V2CreateView(CreateView, SuccessMessageMixin):
    model = Criteria
    # content = {'criterias': Criteria.objects.all()}
    fields = ['RotationType', 'TypeAmount']
    # success_message = "Add new criteria successfully!"
    def get_success_url(self):
        messages.success(self.request, 'Add new criteria successfully!')
        return reverse('criteria-list')

class V2UpdateView(UpdateView):
    model = Criteria
    # content = {'criterias': Criteria.objects.all()}
    fields = ['RotationType', 'TypeAmount']
    def get_success_url(self):
        messages.success(self.request, 'Edit criteria successfully!')
        return reverse('criteria-list')
