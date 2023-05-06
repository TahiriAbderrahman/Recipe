from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Recette
from faker import Faker
from .form import RecetteForm

f= Faker()


def list_recette(request):

    #for i in range(10):
     #   Recette(None,f.name(),).save()
    recette = Recette.objects.all()
    return render(request, 'recette.html' , {'recette':recette})


def create_recette(request):
    if request.method == 'POST':
        form = RecetteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recette')
    else:
        form = RecetteForm()
        return render(request, 'create_recette.html' , {'form':form})

