from django.shortcuts import render, redirect
from .models import Destination
from .forms import DestinoTuristico
# Create your views here.
def index(request):
    dest = Destination.objects.all()
    return render(request, 'index.html', {'dest': dest})

def lista(request):
    destinos = Destination.objects.all()
    contexto = {
    'destinos':destinos
    }
    return render(request,'lista.html', contexto)

def añadir(request):
    if request.method == 'GET':
        form = DestinoTuristico()
        contexto ={
        'form':form
        }

    else:
        form = DestinoTuristico(request.POST)
        contexto ={
        'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('lista')
    return render(request,'añadir.html', contexto)
def editar(request,id):
    destinos = Destination.objects.get(id=id)
    if request.method == 'GET':
        form = DestinoTuristico(instance = destinos)
        contexto ={
        'form':form
        } 
    else:
        form = DestinoTuristico(request.POST, instance = destinos)
        contexto ={
        'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('lista')
    return render(request, 'añadir.html', contexto)
