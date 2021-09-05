from django.shortcuts import render, HttpResponse
from django.views.generic.base import TemplateView #crude
"""
Inicio home/
Portafolio portfolio/
Contacto contact/

"""

# Create your views here.

def home(request):
    return render(request, "core/home.html")


# vistas crude

class HomePageView(TemplateView):
    template_name ="core/homeCrud.html"
    def get(self,request, *args, **kwargs):   #se pasan los argumentos
        return render(request,self.template_name,{'title':"Inicio Crud"})
    

class SamplePageView(TemplateView):
    template_name = "core/sampleCrud.html"

