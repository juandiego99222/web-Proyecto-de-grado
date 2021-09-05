from django import template
from pages.models import Page

register =template.Library() #se registra el tag en la libreria de templates


@register.simple_tag
def get_page_list():
    pages =Page.objects.all()
    return pages

#obtengo todos los objetos de pages
#aqui se esta creando un template tag con todos los datos de las pages