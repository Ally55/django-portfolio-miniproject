from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

from pprint import pprint

# Create your views here.
def index(request):
    projects = Project.objects.all() # this line gets all the objects from the database
    return render(request, 'portfolio/index.html', {'projects': projects})

