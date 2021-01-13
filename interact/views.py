import csv, io
from django.shortcuts import render
from django.contrib import messages
from django.db.models import Q

# Create your views here.
from .models import *


def home(request):
    
    interactions = Interaction.objects.all()


    if request.method == 'GET':

        searched_protein = request.GET.get('protein')    
        if searched_protein != '' and searched_protein is not None:
            interactions = interactions.filter(protein1__icontains=searched_protein)
        else:
            interactions = interactions


        neighborhood_search = request.GET.get('neighborhood')  
        neighborhood_type = request.GET.get('neighborhood_t')  
        if neighborhood_search != '' and neighborhood_search is not None:
            if neighborhood_type == '1':
                interactions = interactions.filter(neighborhood__lt=neighborhood_search)
            if neighborhood_type == '2':
                interactions = interactions.filter(neighborhood=neighborhood_search)
            if neighborhood_type == '3':
                interactions = interactions.filter(neighborhood__gt=neighborhood_search)
            if neighborhood_type == '4':
                interactions = interactions.filter(neighborhood__ne=neighborhood_search)
            if neighborhood_type == '4':
                interactions = interactions.exclude(neighborhood=neighborhood_search)
        else:
            interactions = interactions


        fusion_search = request.GET.get('fusion')  
        fusion_type = request.GET.get('fusion_t')  
        if fusion_search != '' and fusion_search is not None:
            if fusion_type == '1':
                interactions = interactions.filter(fusion__lt=fusion_search)
            if fusion_type == '2':
                interactions = interactions.filter(fusion=fusion_search)
            if fusion_type == '3':
                interactions = interactions.filter(fusion__gt=fusion_search)
            if fusion_type == '4':
                interactions = interactions.exclude(fusion=fusion_search)
        else:
            interactions = interactions


        coexpression_search = request.GET.get('coexpression')  
        coexpression_type = request.GET.get('coexpression_t')  
        if coexpression_search != '' and coexpression_search is not None:
            if coexpression_type == '1':
                interactions = interactions.filter(coexpression__lt=coexpression_search)
            if coexpression_type == '2':
                interactions = interactions.filter(coexpression=coexpression_search)
            if coexpression_type == '3':
                interactions = interactions.filter(coexpression__gt=coexpression_search)
            if coexpression_type == '4':
                interactions = interactions.exclude(coexpression=coexpression_search)
        else:
            interactions = interactions


        experimental_search = request.GET.get('experimental')  
        experimental_type = request.GET.get('experimental_t')  
        if experimental_search != '' and experimental_search is not None:
            if experimental_type == '1':
                interactions = interactions.filter(experimental__lt=experimental_search)
            if experimental_type == '2':
                interactions = interactions.filter(experimental=experimental_search)
            if experimental_type == '3':
                interactions = interactions.filter(experimental__gt=experimental_search)
            if experimental_type == '4':
                interactions = interactions.exclude(experimental=experimental_search)
        else:
            interactions = interactions


        textmining_search = request.GET.get('textmining')  
        textmining_type = request.GET.get('textmining_t')  
        if textmining_search != '' and textmining_search is not None:
            if textmining_type == '1':
                interactions = interactions.filter(textmining__lt=textmining_search)
            if textmining_type == '2':
                interactions = interactions.filter(textmining=textmining_search)
            if textmining_type == '3':
                interactions = interactions.filter(textmining__gt=textmining_search)
            if textmining_type == '4':
                interactions = interactions.exclude(textmining=textmining_search)
        else:
            interactions = interactions



        combined_score_search = request.GET.get('combined_score')  
        combined_score_type = request.GET.get('combined_score_t')  
        if combined_score_search != '' and combined_score_search is not None:
            if combined_score_type == '1':
                interactions = interactions.filter(combined_score__lt=combined_score_search)
            if combined_score_type == '2':
                interactions = interactions.filter(combined_score=combined_score_search)
            if combined_score_type == '3':
                interactions = interactions.filter(combined_score__gt=combined_score_search)
            if combined_score_type == '4':
                interactions = interactions.exclude(combined_score=combined_score_search)
        else:
            interactions = interactions


        cooccurance_search = request.GET.get('cooccurance')  
        cooccurance_type = request.GET.get('cooccurance_t')  
        if cooccurance_search != '' and cooccurance_search is not None:
            if cooccurance_type == '1':
                interactions = interactions.filter(cooccurance__lt=cooccurance_search)
            if cooccurance_type == '2':
                interactions = interactions.filter(cooccurance=cooccurance_search)
            if cooccurance_type == '3':
                interactions = interactions.filter(cooccurance__gt=cooccurance_search)
            if cooccurance_type == '4':
                interactions = interactions.exclude(cooccurance=cooccurance_search)
        else:
            interactions = interactions


        database_search = request.GET.get('database')  
        database_type = request.GET.get('database_t')  
        if database_search != '' and database_search is not None:
            if database_type == '1':
                interactions = interactions.filter(database__lt=database_search)
            if database_type == '2':
                interactions = interactions.filter(database=database_search)
            if database_type == '3':
                interactions = interactions.filter(database__gt=database_search)
            if database_type == '4':
                interactions = interactions.exclude(database=database_search)
        else:
            interactions = interactions



        if searched_protein is None:
            searched_protein = ''

        if neighborhood_search is None:
            neighborhood_search = ''

        if fusion_search is None:
            fusion_search = ''        


        if combined_score_search is None:
            combined_score_search = ''
    
        if textmining_search is None:
            textmining_search = ''

        if coexpression_search is None:
            coexpression_search = ''
    
        if experimental_search is None:
            experimental_search = ''

        if cooccurance_search is None:
            cooccurance_search = ''
    
        if database_search is None:
            database_search = ''


        context = {
            'interactions': interactions ,
            'searched_protein' : searched_protein ,
            'combined_score_type': combined_score_type ,
            'combined_score_search': combined_score_search,
            'textmining_type': textmining_type ,
            'textmining_search': textmining_search,
            'neighborhood_type': neighborhood_type ,
            'neighborhood_search': neighborhood_search,
            'fusion_type': fusion_type ,
            'fusion_search': fusion_search,
            'coexpression_type': coexpression_type ,
            'coexpression_search': coexpression_search,
            'experimental_type': experimental_type ,
            'experimental_search': experimental_search,
            'cooccurance_type': cooccurance_type ,
            'cooccurance_search': cooccurance_search,
            'database_type': database_type ,
            'database_search': database_search
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


