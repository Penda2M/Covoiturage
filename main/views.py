from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import * 
from django.views.generic import CreateView
from main.forms import TrajetForm

def index(request):
   # return HttpResponse("Hello, world. You're at the polls index.")
   return render(request, 'main/index.html')

def trajets(request):
    #recupration des trajets
    trajets = Trajet.objects.all()
    return render(request, 'main/trajets.html', {'trajets': trajets})

def trajet_detail(request, id):
    trajet = Trajet.objects.get(id=id)
    print(trajet.passager.all())
    return render(request, 'main/trajet_detail.html', {'trajet': trajet})

def conducteurs(request):
    conducteurs = Conducteur.objects.all()
    return render(request, 'main/conducteurs.html', {'conducteurs': conducteurs})

def un_conducteur(request, id):
    conducteur = Conducteur.objects.get(id=id)
   # print(conducteur.trajet_set.all())
    return render(request, 'main/un_conducteur.html', {'conducteur': conducteur})

def passagers(request):
    passagers = Passager.objects.all()
    return render(request, 'main/passagers.html', {'passagers': passagers})

def un_passager(request, id):
    passager = Passager.objects.get(id=id)
    return render(request, 'main/un_passager.html', {'passager': passager})    

def nouveau_trajet_conducteur(request):

    trajet = TrajetForm()
    context = {'trajet': trajet}
    if request.method == 'POST':
        #print('printing post = ', request.POST)
        trajet = TrajetForm(request.POST)
        if trajet.is_valid():
            trajet.save()
            return render(request, 'main/nouveau_trajet_conducteur.html', context)


    return render(request, 'main/nouveau_trajet_conducteur.html', context)


def update_trajet(request, id):
    trajet = Trajet.objects.get(id=id)
    trajet = TrajetForm(instance=trajet)

    if request.method == 'POST':
        #print('printing post = ', request.POST)
        trajet = TrajetForm(request.POST, instance=trajet)
        if trajet.is_valid():
            trajet.save()
            return render(request, 'main/trajets.html', {'trajet': trajet})
    return render(request, 'main/update_trajet.html', {'trajet': trajet})

def delete_trajet(request, id):
    trajet = Trajet.objects.get(id=id)
    context = {'item': trajet}

    if request.method == 'POST':
        trajet.delete()
        return render(request, 'main/index.html', {'trajet': trajet})
    return render(request, 'main/delete_trajet.html', context)