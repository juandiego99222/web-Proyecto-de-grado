"""PMO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from PMO.settings import MEDIA_ROOT
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from portfolio.urls import projects_patterns
from profiles.urls import profiles_patterns
from messenger.urls import messenger_patterns
from documentos.urls import documentos_patterns
from django.conf.urls import url
from django.views.static import serve


urlpatterns = [

    #paths del core
    path('', include('core.urls')),
    #paths del portfolio
    path('portfolio/', include('portfolio.urls')),
    path('projects/', include(projects_patterns)),
    
    #paths del pages
    path('page/', include('pages.urls')),
    #paths del contact
    path('contact/', include('contact.urls')),
    #paths del admin
    path('admin/', admin.site.urls),

    #paths de autenticacion
    path('accounts/', include('django.contrib.auth.urls')), 
    path('accounts/', include('registration.urls')),   #path para el registro de usuarios

    #paths de profiles
    path('profiles/', include(profiles_patterns)),

    #paths de messenger
    path('messenger/', include(messenger_patterns)),

    #paths de subir documentos 
    path('documents/',include(documentos_patterns)),
    url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]


#cargar ficheros media en url
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static (settings.STATIC_URL, document_root = settings.STATIC_ROOT)
