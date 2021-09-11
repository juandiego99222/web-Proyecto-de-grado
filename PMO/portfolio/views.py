
from django import forms
from django.contrib.admin.filters import ListFilter
from django.core.files.base import File
from django.db.models.aggregates import Sum
from django.db.models.fields import files
from django.db.models.query import QuerySet
from django.forms import widgets, formset_factory
from django.shortcuts import render
from .models import Project,Interested,Cost,Hito,Risk,Budget,Schedule,Files
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required #decorador django
from django.utils.decorators import method_decorator #decorador de metodos
#crud
from django.views.generic.list import ListView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse , reverse_lazy
from .forms import ProjectForm,InterestedForm,CostForm,HitoForm,RiskForm,BudgetForm,ScheduleForm,FileForm
from django.db.models import Q
from .filters import ProjectFilter
from django.forms import inlineformset_factory
import os
from django.http import HttpResponse
from django.http.response import Http404

from datetime import datetime
from django.db.models.functions import Coalesce



def portfolio(request):


    projects=Project.objects.all()   #traigo todos los objetos de services para despues pasarlos al template
    return render(request, "portfolio/portfolio.html", {'projects' : projects})

"""
class StaffRequiredMixin(object):
    #un mixin es una implementacion de varias funcionalidades para una clase para despues estas heredarlas a otras clases creadas, sirve para no crear los mismos metodos en todas las clases
    #este mixin requerira que el usuario sea miembro del staff
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff: # si el usuario no esta identificado me lleva al admin
            return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)#esta funcion se encarga de dovolverme el usuario identificado al yo hacer la peticion create, update o delete, para que luego no me permita acceder a create si el usuario no esta identificado en el admin
    #class ProyectoCreate(StaffRequiredMixin, CreateView):  #asi heredo el mixin para que funcione en otra clase
"""

class StaffRequiredMixin(object):
    #un mixin es una implementacion de varias funcionalidades para una clase para despues estas heredarlas a otras clases creadas, sirve para no crear los mismos metodos en todas las clases
    #este mixin requerira que el usuario sea miembro del staff
    method_decorator(staff_member_required)#aqui importo el decorados para que cuando me registre me lleve a la otra pagina 
    def dispatch(self, request, *args, **kwargs):
        #como se puede observar el decorador me ahorra el metodo if anteriormente hecho
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs) #esta funcion se encarga de dovolverme el usuario identificado al yo hacer la peticion create, update o delete, para que luego no me permita acceder a create si el usuario no esta identificado en el admin
        
    #class ProyectoCreate(StaffRequiredMixin, CreateView):  #asi heredo el mixin para que funcione en otra clase

# Crud


@method_decorator(staff_member_required, name='dispatch')#asi agrego el decorador a la clase
class ProyectoListView (ListView):
    model = Project
    template_name= 'portfolio/project_list.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProjectFilter(self.request.GET, queryset=self.get_queryset())


        return context



@method_decorator(staff_member_required, name='dispatch')#asi agrego el decorador a la clase
class ProyectoDetailView(DetailView):
    model= Project
    
    
    def get_context_data(self, **kwargs):
        
        pk =self.kwargs.get('pk', 0)
        context = super().get_context_data(**kwargs)
        
        context['interested'] = Interested.objects.filter(project_id=pk)
        context['hitos'] = Hito.objects.get(project_id=pk)
        context['riesgos'] = Risk.objects.filter(project_id=pk)
        
        
        countertareasterminadas = Schedule.objects.filter(estado= "Terminada",project_id=pk).count
        counterTareasTotal =Schedule.objects.filter(project_id=pk).count

        context['aaa']=countertareasterminadas
        context['bbb']=counterTareasTotal
        return context



#https://dev.to/zxenia/django-inline-formsets-with-class-based-views-and-crispy-forms-14o6
#https://medium.com/@adandan01/django-inline-formsets-example-mybook-420cc4b6225d
@method_decorator(staff_member_required, name='dispatch')#asi agrego el decorador a la clase
class ProyectoCreate(CreateView): 
    
    model = Project
    form_class =ProjectForm #contenido para la pagina create(form)
    four_form_class= HitoForm
    six_form_class= BudgetForm

    success_url=reverse_lazy('projects:projects')

    
    def get_context_data(self,**kwargs):
        context = super(ProyectoCreate,self).get_context_data(**kwargs)
        
        form_cost_factory= inlineformset_factory(Project,Cost,form=CostForm,extra=1)
        form_cost= form_cost_factory()

        form_schedule_factory= inlineformset_factory(Project,Schedule,form=ScheduleForm,extra=1)
        form_schedule= form_schedule_factory()
       
        form_risk_factory= inlineformset_factory(Project,Risk,form=RiskForm,extra=1)
        form_risk= form_risk_factory()

        form_interested_factory= inlineformset_factory(Project,Interested,form=InterestedForm,extra=1)
        form_interested= form_interested_factory()

        if 'form' not in context:
            context['form']= self.form_class(self.request.GET)      
        if 'form4' not in context:
            context['form4']= self.four_form_class(self.request.GET)
        if 'form6' not in context:
            context['form6']= self.six_form_class(self.request.GET)
        if 'form_cost' not in context:
            context['form_cost']= form_cost
        if 'form_schedule' not in context:
            context['form_schedule']= form_schedule
        if 'form_risk' not in context:
            context['form_risk']= form_risk
        if 'form_interested' not in context:
            context['form_interested']= form_interested
        
        return context
    #guardar en la base de datos y hacer que se guarde para el proyecto que se esta creando con el id en las foraneas de todos
    def post (self,request, *args, **kwargs):
        self.object= self.get_object
        form =self.form_class(request.POST)
        form4 =self.four_form_class(request.POST)
        form6 =self.six_form_class(request.POST)
        form_cost_factory= inlineformset_factory(Project,Cost,form=CostForm,extra=3)
        form_cost= form_cost_factory(request.POST)
        form_schedule_factory= inlineformset_factory(Project,Schedule,form=ScheduleForm,extra=3)
        form_schedule= form_schedule_factory(request.POST)
        form_risk_factory= inlineformset_factory(Project,Risk,form=RiskForm,extra=3)
        form_risk= form_risk_factory(request.POST)
        form_interested_factory= inlineformset_factory(Project,Interested,form=InterestedForm,extra=3)
        form_interested= form_interested_factory(request.POST)

        if form.is_valid() and form_interested.is_valid() and  form4.is_valid() and  form6.is_valid() and form_cost.is_valid() and form_schedule.is_valid() and form_risk.is_valid():
            project= form.save()   
            hito1= form4.save(commit=False)
            hito1.project = form.save()
            hito1.save()
            presupuesto1= form6.save(commit=False)
            presupuesto1.project = form.save()
            presupuesto1.save()         
            form_cost.instance= project
            form_cost.save()
            form_schedule.instance= project
            form_schedule.save()
            form_risk.instance= project
            form_risk.save()
            form_interested.instance= project
            form_interested.save()
              
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form_interested=form_interested,form4=form4,form6=form6,form_cost=form_cost,form_schedule=form_schedule,form_risk=form_risk))

    


@method_decorator(staff_member_required, name='dispatch')#asi agrego el decorador a la clase
class ProyectoUpdate(StaffRequiredMixin,UpdateView):
    model = Project
    second_model= Interested
    third_model= Cost
    four_model= Hito
    
    six_model= Budget
    form_class =ProjectForm
    template_name_suffix='_update_form'
    second_form_class= InterestedForm
    four_form_class= HitoForm
    five_form_class= RiskForm
    six_form_class= BudgetForm
    
    
    def get_context_data(self,**kwargs):
        context = super(ProyectoUpdate,self).get_context_data(**kwargs)
        pk =self.kwargs.get('pk', 0)
        project=Project.objects.filter(id= pk).first()


        hito= self.four_model.objects.get(project_id=pk)
        
        presupuesto= self.six_model.objects.get(project_id=pk)

        form_cost_factory= inlineformset_factory(Project,Cost,form=CostForm,extra=0)
        form_cost= form_cost_factory(instance=project)

        form_schedule_factory= inlineformset_factory(Project,Schedule,form=ScheduleForm,extra=0)
        form_schedule= form_schedule_factory(instance=project)
    
        form_risk_factory= inlineformset_factory(Project,Risk,form=RiskForm,extra=0)
        form_risk= form_risk_factory(instance=project)

        form_interested_factory= inlineformset_factory(Project,Interested,form=InterestedForm,extra=0)
        form_interested= form_interested_factory(instance=project)

        if 'form' not in context:
            context['form']= self.form_class(instance=project)
        if 'form_cost' not in context:
            context['form_cost']= form_cost
        if 'form4' not in context:
            context['form4']= self.four_form_class(instance=hito)
        if 'form6' not in context:
            context['form6']= self.six_form_class(instance=presupuesto)
        if 'form_schedule' not in context:
            context['form_schedule']= form_schedule
        if 'form_risk' not in context:
            context['form_risk']= form_risk
        if 'form_interested' not in context:
            context['form_interested']= form_interested
        
        context['id']=pk
        
        return context


    def get_success_url(self):
        return reverse_lazy('projects:projects') 

    def post(self, request, *args, **kwargs):
        self.object=self.get_object
        pk =self.kwargs.get('pk', 0)
        project=Project.objects.get(id= pk)
        
        
        hito= self.four_model.objects.get(project_id=pk)
        presupuesto= self.six_model.objects.get(project_id=pk)


        form=self.form_class(request.POST, instance=project)
        form4=self.four_form_class(request.POST, instance=hito)
        form6=self.six_form_class(request.POST, instance=presupuesto)

        form_cost_factory= inlineformset_factory(Project,Cost,form=CostForm,extra=3)
        form_cost= form_cost_factory(request.POST,instance=project)

        form_schedule_factory= inlineformset_factory(Project,Schedule,form=ScheduleForm,extra=3)
        form_schedule= form_schedule_factory(request.POST,instance=project)

        form_risk_factory= inlineformset_factory(Project,Risk,form=RiskForm,extra=3)
        form_risk= form_risk_factory(request.POST,instance=project)

        form_interested_factory= inlineformset_factory(Project,Interested,form=InterestedForm,extra=3)
        form_interested= form_interested_factory(request.POST,instance=project)
        
        if  form.is_valid() and form_interested.is_valid() and form_cost.is_valid() and form4.is_valid()  and form6.is_valid() and form_schedule.is_valid() and form_risk.is_valid() :
            
            form.save()
            form_interested.save()
            form_cost.save()
            form4.save()
            form6.save()
            form_schedule.save()
            form_risk.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form_interested=form_interested,form4=form4,form6=form6,form_cost=form_cost,form_schedule=form_schedule,form_risk=form_risk))



@method_decorator(staff_member_required, name='dispatch')#asi agrego el decorador a la clase    
class ProyectoDelete(StaffRequiredMixin, DeleteView):
    model = Project
    success_url=reverse_lazy('projects:projects')



@method_decorator(staff_member_required, name='dispatch')#asi agrego el decorador a la clase
class ProyectoRecursosDetailView(DetailView):
    model= Project
    
    template_name_suffix='_detail_recursos'
    
    def get_context_data(self, **kwargs):
        third_model= Cost
        pk =self.kwargs.get('pk', 0)
        context = super().get_context_data(**kwargs)
        
        context['costos'] = Cost.objects.filter(project_id=pk)
        context['presupuesto'] = Budget.objects.get(project_id=pk)
        
        return context


@method_decorator(staff_member_required, name='dispatch')#asi agrego el decorador a la clase
class ProyectoRiesgosDetailView(DetailView):
    model= Project
    
    template_name_suffix='_detail_riesgos'
    
    def get_context_data(self, **kwargs):
        
        pk =self.kwargs.get('pk', 0)
        context = super().get_context_data(**kwargs)
        
        context['riesgos'] = Risk.objects.filter(project_id=pk)
        
        RiesgoBajo1=  Risk.objects.filter(impacto= "Bajo",probabilidad="Baja",project_id=pk)
        RiesgoBajo2=  Risk.objects.filter(impacto= "Medio",probabilidad="Baja",project_id=pk)
        RiesgoBajo3=  Risk.objects.filter(impacto= "Bajo",probabilidad="Media",project_id=pk)

        RiesgoModerado1 = Risk.objects.filter(impacto= "Alto",probabilidad="Baja",project_id=pk)
        RiesgoModerado2 = Risk.objects.filter(impacto= "Medio",probabilidad="Media",project_id=pk)
        RiesgoModerado3 = Risk.objects.filter(impacto= "Bajo",probabilidad="Alta",project_id=pk)

        RiesgoImportante1 = Risk.objects.filter(impacto= "Alto",probabilidad="Media",project_id=pk)
        RiesgoImportante2 = Risk.objects.filter(impacto= "Medio",probabilidad="Alta",project_id=pk)

        RiesgoIntolerable = Risk.objects.filter(impacto= "Alto",probabilidad="Alta",project_id=pk)

        context['RiesgoBajo1']=RiesgoBajo1
        context['RiesgoBajo2']=RiesgoBajo2
        context['RiesgoBajo3']=RiesgoBajo3
        context['RiesgoModerado1']=RiesgoModerado1
        context['RiesgoModerado2']=RiesgoModerado2
        context['RiesgoModerado3']=RiesgoModerado3
        context['RiesgoImportante1']=RiesgoImportante1
        context['RiesgoImportante2']=RiesgoImportante2
        context['RiesgoIntolerable']=RiesgoIntolerable
        
        
        return context

    
@method_decorator(staff_member_required, name='dispatch')#asi agrego el decorador a la clase
class ProyectoInteresadosDetailView(DetailView):
    model= Project
    
    template_name_suffix='_detail_interesados'
    
    def get_context_data(self, **kwargs):
        
        pk =self.kwargs.get('pk', 0)
        context = super().get_context_data(**kwargs)
        
        context['interesados'] = Interested.objects.filter(project_id=pk)
        
        observar=  Interested.objects.filter(interes= "Bajo",influencia="Baja",project_id=pk)
        satisfacer= Interested.objects.filter(interes= "Alto",influencia="Baja",project_id=pk)
        comunicar= Interested.objects.filter(interes= "Bajo",influencia="Alta",project_id=pk)
        colaborar= Interested.objects.filter(interes= "Alto",influencia="Alta",project_id=pk)

        context['observar']=observar
        context['satisfacer']=satisfacer
        context['comunicar']=comunicar
        context['colaborar']=colaborar
               
        
        return context
 
@method_decorator(staff_member_required, name='dispatch')#asi agrego el decorador a la clase
class ArchivoCreate(StaffRequiredMixin,CreateView): 
    
    model = Files
    form_class =FileForm
    template_name= 'portfolio/subirArchivo.html'
    success_url=reverse_lazy('projects:projects')
    
    def get_form(self, form_class = None):
        
        pk =self.kwargs.get('pk', 0)
        form = super().get_form(form_class)
        form.fields['project'].disabled = True
        form.fields['project'].initial = pk
       
        return form
    

    
@method_decorator(staff_member_required, name='dispatch')#asi agrego el decorador a la clase
class ProyectoArchivosDetailView(DetailView):
    model= Project
    
    template_name= 'portfolio/descargarArchivos.html'
    
    def get_context_data(self, **kwargs):
        third_model= File
        pk =self.kwargs.get('pk', 0)
        context = super().get_context_data(**kwargs)
        
        context['file'] = Files.objects.filter(project_id=pk)
        
        return context

def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exist(file_path):
        with open(file_path,'rb') as fh:
            response= HttpResponse(fh.read(),content_type="application/upload")
            response['Content-disposition']='inline;filename'+os.path.basename(file_path)
            return response
    
    raise Http404
   

@method_decorator(staff_member_required, name='dispatch')#asi agrego el decorador a la clase
class ScheduleDetailView (DetailView):
    model = Project
    template_name= 'portfolio/project_list_cronograma.html'
    

    def get_context_data(self, **kwargs):
        
        pk =self.kwargs.get('pk', 0)
        context = super().get_context_data(**kwargs)
        
        context['actividad'] = Schedule.objects.filter(project_id=pk)

        return context


class IndicadoresDetailView(DetailView):
    model = Project
    template_name = 'portfolio/project_detail_indicadores.html'

    def get_reporte_costos_meses(self, **kwargs):
        data =[]
        try:
            pk =self.kwargs.get('pk', 0)
            totalcosto= Cost.objects.filter(project_id=pk).aggregate(r=Coalesce(Sum('amountCost'),0)).get('r')
            data.append(float(totalcosto))  
        except:
            pass
        return data

    

    def get_context_data(self, **kwargs):
        
        pk =self.kwargs.get('pk', 0)
        context = super().get_context_data(**kwargs)
        
        context['reporte_costos_meses'] = self.get_reporte_costos_meses()
        context['presupuesto'] = Budget.objects.get(project_id=pk)
        
        context['tareasSinComenzar'] = Schedule.objects.filter(project_id=pk, estado= "Sin empezar").count
        context['tareasEnProgreso'] = Schedule.objects.filter(project_id=pk, estado= "En Progreso").count
        context['tareasTerminadas'] = Schedule.objects.filter(project_id=pk, estado= "Terminada").count

        return context



#vista de inline formet para cronograma
def crearCronograma(request):
    
    if request.method == "GET":
        
        form_schedule_factory = inlineformset_factory(Project,Schedule,form=ScheduleForm,extra=1)
        form_schedule= form_schedule_factory() 
        context={
            'form_schedule':form_schedule,
            
        }
        return render(request,"",context)

    elif request.method =="POST":
        form_schedule_factory = inlineformset_factory(Project,Schedule,form=ScheduleForm)
        form_schedule= form_schedule_factory(request.POST)

        if form_schedule.is_valid():

            form_schedule.save()
            return redirect(reverse('projects:projects'))
        else:
            context ={
                'form_schedule':form_schedule,
            }
            return render(request, "portfolio/project_create_cronograma.html",context )
