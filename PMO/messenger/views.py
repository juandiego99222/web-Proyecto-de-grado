from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Thread,Message
from django.views.generic import TemplateView
from django.http import Http404, JsonResponse

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.

@method_decorator(login_required, name="dispatch")
class ThreadList(TemplateView):     #listar todos los hilos de un usuario
    template_name= "messenger/thread_list.html"

     
@method_decorator(login_required, name="dispatch")
class ThreadDetail(DetailView): #listar mensajes de un hilo
    model= Thread

    def get_object(self):
        obj=super(ThreadDetail,self).get_object()
        if self.request.user not in obj.users.all():        #si el usuario que esta identificado no forma parte del hilo
            raise Http404()                                 #se le mostrara un error 404
        return obj

def add_message(request, pk ): #cuando se añada un mensaje se devolvera una respuesta el cual es el json_response.
    json_response={'created': False}   #diccionario para estructurar respuesta json, si el mensaje se crea correctamente se cambiara el valor del diccionario a true y si no se lo dejara como false
    if request.user.is_authenticated:
        content=request.GET.get('content',None) #obtengo el contenido de content
        if content:                             #si si hay contenido
            thread = get_object_or_404(Thread,pk=pk) #recuperamos el hilo
            message= Message.objects.create(user=request.user,content=content) #se crea el mensaje con el contenido
            thread.messages.add(message)#se agregar el contenido al hilo
            json_response['created']=True   #se cambia el json a true especificando que el mensaje se crea correctamente
            if len(thread.messages.all()) is 1:
                json_response['first']= True
    else:
        raise Http404("User is not authenticated")
    return JsonResponse(json_response) #convierte de diccionario python a objeto de tipo JSON

@login_required
def start_thread(request,username):         #iniciar hilo
    user= get_object_or_404(User, username=username)
    thread= Thread.objects.find_or_create(user, request.user)  # se crea un hilo entre el user: el usuario con el que queremos chatear y el request.user osea nosotros
    return redirect(reverse_lazy('messenger:detail',args=[thread.pk]))