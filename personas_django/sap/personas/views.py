from django.shortcuts import render,get_object_or_404,redirect
from personas.models import Persona,Domicilio
from django.forms import modelform_factory
from personas.forms import PersonaForm,DomicilioForm

def detallePersona(request,id):
    personas = get_object_or_404(Persona,pk=id)
    sin_registrar = 'No registrado'
    try:
        domicilio = Domicilio.objects.get(pk=personas.domicilio_id)
        return render(request,'personas/detalle.html',{'persona': personas,'domicilio': domicilio.id})
    except:
        return render(request,'personas/detalle.html',{'persona': personas,'domicilio': sin_registrar})

def nuevaPersona(request):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('listperson')
    else:
        formaPersona = PersonaForm()

    return render(request,'personas/nuevo.html',{'formaPersona': formaPersona})

def editarPersona(request,id):
    persona = get_object_or_404(Persona,pk=id)
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST,instance=persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('listperson')
    else:
        formaPersona = PersonaForm(instance=persona)

    return render(request,'personas/editar.html',{'formaPersona': formaPersona})

def eliminarPersona(request,id):
    persona = get_object_or_404(Persona,pk=id)
    if persona:
        persona.delete()
    return redirect('listperson')

def domicilios(request):
    domicilios = Domicilio.objects.all()
    nro_domi = Domicilio.objects.count()
    return render(request,'personas/domicilios.html',{'domicilios': domicilios,'numero':nro_domi})

def nuevoDomicilio(request):
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('listado')
    else:
        formaDomicilio = DomicilioForm()

    return render(request,'personas/nuevo-domicilio.html',{'formaDomicilio': formaDomicilio})

def editarDomicilio(request,id):
    domicilio = get_object_or_404(Domicilio,pk=id)
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST,instance=domicilio)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('listado')
    else:
        formaDomicilio = DomicilioForm(instance=domicilio)

    return render(request,'personas/editar-domicilio.html',{'formaDomicilio': formaDomicilio})

def eliminarDomicilio(request,id):
    domicilio = get_object_or_404(Domicilio,pk=id)
    if domicilio:
        domicilio.delete()
    return redirect('listado')
