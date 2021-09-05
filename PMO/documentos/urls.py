from django.urls import path
from . import views
from .views import ArchivoCreate

#crud
documentos_patterns = ([
    
  path('', views.home, name="documents"),
  path('create/', ArchivoCreate.as_view(), name='create'),
    
], 'documents')