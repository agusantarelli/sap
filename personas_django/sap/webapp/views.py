from django.shortcuts import render
from django.http import HttpResponse
from personas.models import Persona

# Create your views here.


def personas(request):
    nro_personas = Persona.objects.count()
    personas_var = Persona.objects.all()
    return render(request, 'bienvenido.html',{'Numero': nro_personas, 'personas': personas_var})

def bienvenidopro(request):
    return render(request,'bienvenidopro.html')

def about(request):
    return render(request,'about.html')
'''
def despedirse(request):
    return HttpResponse('Despedida desde Django')

def contacto(request):
    return HttpResponse('Telefono: 3571520433\n Email: santarelliagustina98@gmail.com')
'''
