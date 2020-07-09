from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dest = Destination.objects.all()
    return render(request, 'index.html', {'dest': dest})

def lista(request):
    destino = Destination.objects.all()
    contexto = {
    'destino':destino
    }
    return render(request,'lista.html', contexto)
