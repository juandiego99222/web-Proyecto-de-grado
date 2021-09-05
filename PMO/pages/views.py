from django.shortcuts import render,get_object_or_404
from .models import Page
# Create your views here.

def page(request, page_id, page_slug):
    page= get_object_or_404(Page, id=page_id)  #get nos permite cojer un unico registro: en este caso el id
    return render(request,"pages/sample.html", {'page':page})
