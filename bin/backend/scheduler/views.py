from django.shortcuts import render
from .models import Criteria

def criteria(request):
    return render(request, 'index.html')

def test(request):
    content = {'criterias': Criteria.objects.all()}
    return render(request, 'test.html', content)

# Create your views here.
