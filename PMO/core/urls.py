from django.urls import path
from . import views

from .views import HomePageView,SamplePageView  #crud


urlpatterns = [

    path('', views.home, name="home"),
   
    #crud
    path('inicio/', HomePageView.as_view(), name="inicio"),
    path('sample/', SamplePageView.as_view(), name="sample"),

   
]