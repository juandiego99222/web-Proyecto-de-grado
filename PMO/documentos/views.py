from documentos.forms import FileForm
from django.http.response import Http404
from documentos.models import Files
from django.shortcuts import render
from django.http import HttpResponse
from .models import Files
import os
from django.contrib.admin.views.decorators import staff_member_required #decorador django
from django.utils.decorators import method_decorator #decorador de metodos
from django.views.generic.edit import CreateView
from django.urls import reverse , reverse_lazy
from django.http import HttpResponseRedirect
  
# Create your views here.

def home(request):
    context={'file':Files.objects.all()}
    return render(request,'documentos/documentos.html',context)




def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exist(file_path):
        with open(file_path,'rb') as fh:
            response= HttpResponse(fh.read(),content_type="application/upload")
            response['Content-disposition']='inline;filename'+os.path.basename(file_path)
            return response
    
    raise Http404

@method_decorator(staff_member_required, name='dispatch')#asi agrego el decorador a la clase
class ArchivoCreate( CreateView): 
    
    model = Files
    form_class =FileForm #contenido para la pagina create(form)
    template_name= 'documentos/subirarchivo.html'
    success_url=reverse_lazy('documents:documents')

    

