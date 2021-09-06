from django.urls import path
from . import views

from .views import ProyectoArchivosDetailView, ProyectoListView,ProyectoDetailView,ProyectoCreate,ProyectoUpdate,ProyectoDelete, ProyectoRecursosDetailView,  ScheduleDetailView,ArchivoCreate,ProyectoRiesgosDetailView


urlpatterns = [
    path('', views.portfolio, name="portfolio"),
      
]
#crud
projects_patterns = ([
    
    path('projects/', ProyectoListView.as_view(), name='projects'),
    path('<int:pk>/<slug:slug>/', ProyectoDetailView.as_view(), name='project'), 
    
    path('create/', ProyectoCreate.as_view(), name='create'),
    path('update/<int:pk>/', ProyectoUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', ProyectoDelete.as_view(), name='delete'),

    path('<int:pk>/<slug:slug>/recursos/', ProyectoRecursosDetailView.as_view(), name='recursos'), 

    path('<int:pk>/<slug:slug>/cronograma/', ScheduleDetailView.as_view(), name='cronograma'), 
    
    path('<int:pk>/<slug:slug>/riesgos/',ProyectoRiesgosDetailView.as_view(), name='riesgos'), 

    path('subir/<int:pk>/', ArchivoCreate.as_view(), name='subirA'),
    path('<int:pk>/<slug:slug>/documents/', ProyectoArchivosDetailView.as_view(), name="documents"),

    
], 'projects')