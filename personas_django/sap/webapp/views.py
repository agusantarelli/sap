from django.shortcuts import render
from django.http import HttpResponse
from personas.models import Persona


def personas(request):
    nro_personas = Persona.objects.count()
    personas_var = Persona.objects.all()
    return render(request, 'listadopersonas.html',{'Numero': nro_personas, 'personas': personas_var})

def bienvenido(request):
    return render(request,'menu.html')

def about(request):
    return render(request,'about.html')
