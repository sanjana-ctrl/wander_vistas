from django.shortcuts import render,get_object_or_404
from .models import destination
# Create your views here.

def index(request):

    dests=destination.objects.all() 
    
    return render(request, 'index.html', {'dests':dests}) 

def explore(request, id):
    dest = get_object_or_404(destination, id=id)
    return render(request, 'explore.html', {'dest': dest})
