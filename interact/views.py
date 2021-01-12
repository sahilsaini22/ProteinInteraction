import csv, io
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from .models import *


def home(request):
    interactions = Interaction.objects.all()

    context = {
        'interactions': interactions        
    }
    return render(request, 'interact/list.html', context)
    

def upload(request):
 #   template: "interact/upload.html"

    if request.method == 'GET':
        return render(request, "interact/upload.html")

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request,'Incorrect file format')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    i = 0    
    #print(len(thislist))
    for column in csv.reader(io_string, delimiter=','): 
        i = i + 1
        _, Created = Interaction.objects.update_or_create(
        id = column[0], 
        coexpression = column[1] ,
        combined_score = column[2], 
        cooccurance = column[3] ,
        database = column[4] ,
        experimental = column[5] ,
        fusion = column[6] ,
        neighborhood = column[7] ,
        protein1 = column[8] ,
        protein2 = column[9] ,
        textmining = column[10] 
        )
    print(i)
    context = {}

    return render(request, "interact/upload.html"   , context)
