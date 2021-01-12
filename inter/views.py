from django.shortcuts import render

# Create your views here.
from .models import *


def home(request):
    interactions = Interaction.objects.all()

    context = {
        'interactions': interactions        
    }
    return render(request, 'inter/list.html', context)
    

