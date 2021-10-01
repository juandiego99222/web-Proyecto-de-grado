from django.db import models
from django.db.models.enums import Choices
from django.utils.timezone import now #zona horaria actual
from django.contrib.auth.models import User # trae a todos los usuarios registrados en administrador
from ckeditor.fields import RichTextField
# Create your models here.

 

class Phase(models.Model):
    name = models.CharField(max_length=200, verbose_name= "Nombre")
    class Meta:
        verbose_name ="fase"
        verbose_name_plural= "fases"   #verbose_name = cambia el nombre por el elegido, en este caso a español
    def __str__(self):
        return self.name  



class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name= "Nombre Proyecto")
    content= models.TextField(verbose_name="Descripcion")
    author=models.ForeignKey(User,verbose_name="Encargado", on_delete= models.SET_NULL, null=True)
    phase= models.ForeignKey(Phase, verbose_name="Fase", on_delete=models.SET_NULL, null=True)
    created= models.DateTimeField(verbose_name="Fecha de creacion",  default=now)
    completed= models.DateTimeField(verbose_name="Fecha de finalizacion",  default=now)
    alcance= models.TextField(verbose_name="Alcance",null=True)
    objetivos= models.TextField(verbose_name="Objetivos",null=True)
    estado=models.CharField(max_length=32,null=True,choices=[
        ('Iniciado','Iniciado'),
        ('En Progreso','En Progreso'),
        ('Terminado','Terminado'),
        ('Inactivo','Inactivo'),
    ])
    
    class Meta:
        verbose_name ="proyecto"
        verbose_name_plural= "proyectos"   #verbose_name = cambia el nombre por el elegido, en este caso a español
        ordering = ['-created'] #ordenar por fecha de creacion
    def __str__(self):
        return self.title     #devolvemos el titulo en la tabla



class Interested(models.Model):
    name = models.CharField(max_length=200, verbose_name= "")
    interes=models.CharField(max_length=32,null=True,choices=[
        ('Bajo','Bajo'),
        ('Alto','Alto'),
    ])
    influencia=models.CharField(max_length=32,null=True,choices=[
        ('Baja','Baja'),
        ('Alta','Alta'),
    ])
    project= models.ForeignKey(Project, verbose_name="Proyecto", on_delete=models.CASCADE,null=True)
    class Meta:
        verbose_name ="interesado"
        verbose_name_plural= "interesados"   #verbose_name = cambia el nombre por el elegido, en este caso a español
    def __str__(self):
        return self.name  




class Cost(models.Model):
    descriptionCost = models.CharField(max_length=200, verbose_name= "")
    amountCost= models.IntegerField(verbose_name="Valor")
    project= models.ForeignKey(Project, verbose_name="Proyecto", on_delete=models.CASCADE ,null=True)
    #unidad  
    #valor
    class Meta:
        
        verbose_name ="costo"
        verbose_name_plural= "costos"   #verbose_name = cambia el nombre por el elegido, en este caso a español
    def __str__(self):
        return self.descriptionCost





class Hito(models.Model):
    descriptionHito = models.CharField(max_length=400, verbose_name= "Descripción Hito")
    project= models.ForeignKey(Project, verbose_name="Proyecto", on_delete=models.CASCADE ,null=True)
    class Meta:
        verbose_name ="hito"
        verbose_name_plural= "hitos"   #verbose_name = cambia el nombre por el elegido, en este caso a español
    def __str__(self):
        return self.descriptionHito  




class Risk(models.Model):
    descriptionRisk = models.CharField(max_length=400, verbose_name= "")
    project= models.ForeignKey(Project, verbose_name="Proyecto", on_delete=models.CASCADE,null=True)
    impacto=models.CharField(max_length=32,null=True,choices=[
        ('Bajo','Bajo'),
        ('Medio','Medio'),
        ('Alto','Alto'),
    ])
    probabilidad=models.CharField(max_length=32,null=True,choices=[
        ('Baja','Baja'),
        ('Media','Media'),
        ('Alta','Alta'),
    ])
    class Meta:
        verbose_name ="riesgo"
        verbose_name_plural= "riesgos"   #verbose_name = cambia el nombre por el elegido, en este caso a español
    def __str__(self):
        return self.descriptionRisk





class Budget(models.Model):
    descriptionBudget = models.CharField(max_length=200, verbose_name= "Descripción Presupuesto")
    project= models.ForeignKey(Project, verbose_name="Proyecto", on_delete=models.CASCADE,null=True)
    amountBudget= models.IntegerField(verbose_name="Cantidad en Pesos")
    #unidad
    
    class Meta:
        verbose_name ="presupuesto"
        verbose_name_plural= "presupuestos"   #verbose_name = cambia el nombre por el elegido, en este caso a español
    def __str__(self):
        return self.descriptionBudget

#cronograma de actividades
class Schedule(models.Model):
    descriptionSchedule = models.CharField(max_length=200, verbose_name= "",null=True)
    created= models.DateTimeField(verbose_name="Fecha Inicio",  default=now,null=True)
    completed= models.DateTimeField(verbose_name="Fecha Fin",  default=now,null=True)
    estado=models.CharField(max_length=32,null=True,choices=[
        ('Sin empezar','Sin empezar'),
        ('En Progreso','En Progreso'),
        ('Terminada','Terminada'),
        
    ])
    project= models.ForeignKey(Project, verbose_name="Proyecto", on_delete=models.CASCADE,null=True)
    order = models.SmallIntegerField(verbose_name="Orden", default=0,null=True,blank=True)

    class Meta:
        verbose_name ="cronograma"
        verbose_name_plural= "cronogramas"   #verbose_name = cambia el nombre por el elegido, en este caso a español
        ordering = ['order'] #ordenar por fecha de creacion
    def __str__(self):
        
        return self.descriptionSchedule



class Files(models.Model):
    title=models.CharField(max_length=50)
    upload=models.FileField(upload_to='media',null=True,blank=True)
    url=models.URLField(max_length = 200,null=True,blank=True)
    project= models.ForeignKey(Project, verbose_name="Proyecto", on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title
  














