from os import name
from django import forms
from .models import Project,Interested,Cost,Hito,Risk,Budget, Schedule,Files
from django.forms.models import inlineformset_factory
from ckeditor.fields import RichTextFormField

class ProjectForm(forms.ModelForm):

    class Meta:
        
        model =Project
        fields = ['title','content','alcance','objetivos', 'author', 'phase', 'created', 'completed','estado']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control','rows':3}), 
            'alcance': forms.Textarea(attrs={'class':'form-control','rows':2}), 
            'objetivos': forms.Textarea(attrs={'class':'form-control','rows':2}), 
            'created':forms.SelectDateWidget(attrs={'class':'form-control-sm'}), 
            'completed':  forms.SelectDateWidget(  attrs={'class':'form-control-sm'}),
            
              
        }
       
        

class InterestedForm(forms.ModelForm):

    class Meta:
        model =Interested
        fields = ['name','interes','influencia']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre Interesado'}),
            
            
        }
        
        
class CostForm(forms.ModelForm):

    class Meta:
        model =Cost
        fields = ['descriptionCost','amountCost']
        widgets = {
            'descriptionCost': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descripcion Costo', 'rows':1}),
            
        }

    


class HitoForm(forms.ModelForm):

    class Meta:
        model = Hito
        fields = ['descriptionHito']
        widgets = {
            'descriptionHito': forms.Textarea(attrs={'class':'form-control', 'rows':2}),
        }
        


class RiskForm(forms.ModelForm):

    class Meta:
        model =Risk
        fields = ['descriptionRisk','impacto','probabilidad']
        widgets = {
            'descriptionRisk': forms.TextInput(attrs={'class':'form-control','placeholder':'Descripción Riesgo' }),
        }


class BudgetForm(forms.ModelForm):

    class Meta:
        model =Budget
        fields = ['descriptionBudget','amountBudget']
        widgets = {
            'descriptionBudget': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descripcion Presupuesto', 'rows':2}),
        }
        

class ScheduleForm(forms.ModelForm):
    class Meta:

        model =Schedule
        fields = ['descriptionSchedule','created','completed','estado','project','order']
        widgets = {
            'descriptionSchedule': forms.Textarea(attrs={'class':'form-control','rows':1, 'placeholder':'Actividad'}), 
            'created':forms.SelectDateWidget(attrs={'class':'form-control-sm'}), 
            'completed':  forms.SelectDateWidget(  attrs={'class':'form-control-sm'}),
              
        }



class FileForm(forms.ModelForm):#formulario para perfil
    class Meta:
        model= Files
        fields=['title','upload','url','project']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre Archivo'}),
            
        }