from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.db.models.signals import m2m_changed  #señal 

# Create your models here.
class Message(models.Model):                    #mensaje
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField()
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['created']


class ThreadManager(models.Manager):        #objectmanager, sirve para añadir filtros al model
    def find(self, user1, user2):  #buscamos si el hilo existe
        queryset = self.filter(users=user1).filter(users=user2)
        if len(queryset) > 0:
            return queryset[0]
        return None

    def find_or_create(self, user1, user2):
        thread = self.find(user1, user2)  #buscamos si el hilo existe con el metodo definido antes
        if thread is None:                  #si no existe
            thread = Thread.objects.create() #se lo crea
            thread.users.add(user1, user2)      #se añade los usuarios al hilo
        return thread

    

class Thread(models.Model):                #hilo= es la comunicacion que hay entre usuario y usuario para el envio de mensajes
    users=models.ManyToManyField(User, related_name='threads')#almacena los usuarios
    messages=models.ManyToManyField(Message)            #almacena todos los mensajes que escribiran los usuarios dentro del hilo
    updated= models.DateTimeField(auto_now=True)

    objects=ThreadManager() #añadimos el object manager al modelo

    class Meta:
        ordering =['-updated']

#señal(test)
def messages_changed(sender,**kwargs):  #comprobar que un mensaje se añada si los usuarios forman parte del hilo, cabe aclarar que el hilo debe ser entre 2 usuarios, por lo cual si un tercer usuario manda un mensaje no deberia añadirse al hilo
    instance= kwargs.pop("instance",None)              #detectar el hilo de los mensajes
    action= kwargs.pop("action",None)                #detectar la accion que se ejecuta, en este caso queremos detectar el momento antes de añadir los mensajes al hilo
    pk_set=  kwargs.pop("pk_set",None)               #identificador de los mensajes que se van a añadir dentro de la relacion many2many
    print(instance, action, pk_set)

    false_pk_set= set()
    if action is "pre_add":
        for msg_pk in pk_set:
            msg =Message.objects.get(pk=msg_pk)
            if msg.user not in instance.users.all():    #si el autor del mensaje no se encuentra dentro de los usuarios que estan añadidos en la instancia del hilo
                print("ups, ({}) no forma parte del hilo".format(msg.user))
                false_pk_set.add(msg_pk) #almacenamos en la variable false_pk los mensajes fraudulentos 

    #buscar los mensajes de false_pk_set que no estan en pk_set y los borramos de pk_set
    pk_set.difference_update(false_pk_set)

    #forzar la actualizacion haciendo un save
    instance.save()

m2m_changed.connect(messages_changed,sender=Thread.messages.through) #conectamos la señal con el model thread 
