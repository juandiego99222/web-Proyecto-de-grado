from django.shortcuts import render,redirect
from .forms import ContactForm  #importo el formulario de contact
from django.urls import reverse #se importa reverse
from django.core.mail import EmailMessage #es la estructura para enviar un mensaje  de email y enviarlo
# Create your views here.


def contact(request):
    contact_form = ContactForm()  #instanciamos el formulario 
    if request.method == "POST":
        contact_form=ContactForm(data=request.POST) #se generaria el formulario automaticamente si enviamos el mensaje
        if contact_form.is_valid():  #comprobamos si los campos estan rellenados correctamente y los llenamos con un post
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            content=request.POST.get('content','')
             #enviamos el correo y redireccionamos
            email=EmailMessage(
                "Oficina de Proyectos:Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name,email,content),
                "oficinadeproyectos2021@gmail.com",
                ["oficinadeproyectos2021@gmail.com","juandiego99222@gmail.com","emronaldom04@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+"?ok") 
            except:
                return redirect(reverse('contact')+"?ok")  #reverse es algo parecido al tag urls, en caso de que se cambie la url no existan problemas
    return render(request, "contact/contact.html",{'form':contact_form})   #y lo enviamos al templeate en un diccionario de contexto