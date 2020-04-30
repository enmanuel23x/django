from django.shortcuts import render
from .models import Carousel,JobOffer,Employees
# Create your views here.
all_JobOffer = JobOffer.objects.all
all_Carousel = Carousel.objects.all
all_Employees = Employees.objects.all

ofertas = ({"autor": "autor1", "titulo": "titulo1", "descripcion": "descripcion1"},
            {"autor": "autor2", "titulo": "titulo2", "descripcion": "descripcion2"},
            {"autor": "autor3", "titulo": "titulo3", "descripcion": "descripcion3"})


def index(request):
   return render(request,'webBeconsult/index.html', {"ofertas":all_JobOffer,"Carousels":all_Carousel,"empleados":all_Employees})

def terminos(request):
   return render(request,'webBeconsult/terminos.html')
