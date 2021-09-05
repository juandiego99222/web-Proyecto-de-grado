from django.contrib import admin
from .models import Project,Interested,Phase,Cost,Hito,Risk,Budget,Schedule,Files

# Register your models here.
# configuracion para el administrador 

class ProjectAdmin(admin.ModelAdmin):
     
    class Media:
        css = {
            'all': ('portfolio/css/custom_ckeditor.css',)
        }
    list_display=('title','author')#mostrar las columnas en la lista
    search_fields= ('id','title','author__username')#formulario de busqueda, para foraneas asi: 'author__username'
    date_hierarchy='created'#utilizar jerarquia de fechas para busquedas
    list_filter= ('author__username', ) #agregar filtro para busqueda
    fieldsets= (
        ("General",{
            "fields":(
                'title','content','author','phase'
            ),
        }),
        ("Fechas",{
            "fields":(
                'created','completed'
            ),
        }),
        
    )
    # Inyectamos nuestro fichero css
    





admin.site.register(Project,ProjectAdmin)
admin.site.register(Interested)
admin.site.register(Phase)
admin.site.register(Cost)
admin.site.register(Hito)
admin.site.register(Risk)
admin.site.register(Budget)
admin.site.register(Schedule)
admin.site.register(Files)
