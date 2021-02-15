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
from django.contrib.auth.mixins import LoginRequiredMixin

#IMPORTED NEW STUFF FROM ARTICLE
from rest_framework.views import APIView 
from rest_framework import status
from rest_framework.response import Response 
from .models import *
from .serializer import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#----------------------------

def criteria(request):
    return render(request, 'scheduler/index.html')

#don't fully understand views but trying to add stuff for the react frontend
class ReactView(APIView):
    serializer_class = ReactSerializer
    
    def get(self, request): 
        TypeAmount = [ {"rotation": TypeAmount.RotationType,"type": TypeAmount.TypeAmount}  
        for TypeAmount in React.objects.all()] 
        return Response(TypeAmount)
    
    def post(self, request): 
        serializer = ReactSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return  Response(serializer.data) 
    
#-----------------------------

class V2ListView(LoginRequiredMixin, ListView):
    login_url = '/admin/login/'
    redirect_field_name = 'redirect_to'
    model = Criteria
    # content = {'criterias': Criteria.objects.all()}
    context_object_name = 'criterias'
    template_name = 'scheduler/test.html'

class V2CreateView(LoginRequiredMixin,CreateView, SuccessMessageMixin):
    login_url = '/admin/login/'
    redirect_field_name = 'redirect_to'
    model = Criteria
    # content = {'criterias': Criteria.objects.all()}
    fields = ['RotationType', 'TypeAmount']
    # success_message = "Add new criteria successfully!"
    def get_success_url(self):
        messages.success(self.request, 'Add new criteria successfully!')
        return reverse('criteria-list')

class V2DetailView(LoginRequiredMixin,DetailView):
    login_url = '/admin/login/'
    redirect_field_name = 'redirect_to'
    model = Criteria
    # fields = ['RotationType', 'TypeAmount']

class V2UpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/admin/login/'
    redirect_field_name = 'redirect_to'
    model = Criteria
    # content = {'criterias': Criteria.objects.all()}
    fields = ['RotationType', 'TypeAmount']
    def get_success_url(self):
        messages.success(self.request, 'Edit criteria successfully!')
        return reverse('criteria-list')

class V2DeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/admin/login/'
    redirect_field_name = 'redirect_to'
    model = Criteria
    success_url = '/scheduler/'
