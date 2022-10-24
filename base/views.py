from django.shortcuts import render, redirect
from base import models
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def alumnos(request):
    alumnos = models.Alumno.objects.all()
    context = {
        'alumnos': alumnos
    }
    return render(request, 'alumno.html', context)
    
    
def notas(request, alumn_id):
    nota = models.Nota.objects.filter(alumno_id=alumn_id).first()
    if nota == None:
        messages.add_message(request, messages.ERROR, 'El Alumno no tiene Nota aun')
        return redirect('index')
    
    context = {
        "nota": nota
    }
    
    return render(request, 'notas.html', context)
