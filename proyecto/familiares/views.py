from django.shortcuts import render

from .models import Pais, Familiar

# Create your views here.

def index(request):
    return render(request, 'familiares/index.html')

def pais_list(request):
    paises = Pais.objects.all()
    contexto = {"paises": paises}
    return render(request, "familiares/pais_list.html", contexto)

def familiares_list(request):
    familiares = Familiar.objects.all()
    contexto = {"familiares": familiares}
    return render(request, "familiares/familiar_list.html", contexto)