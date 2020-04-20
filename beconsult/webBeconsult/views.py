from django.shortcuts import render

# Create your views here.
def index(request):
   return render(request,'index.html')

def terminos(request):
   return render(request,'terminos.html')