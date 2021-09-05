from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


#funcion para borrar la foto anterior cuando se actualiza
def custom_upload_to(instance, filename):
    old_instance =Profile.objects.get(pk=instance.pk)
    old_instance.foto.delete()
    return 'profiles/' + filename

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to=custom_upload_to, null= True, blank=True)
    telefono= models.CharField(null=True,blank=True,max_length=20)
    profesion= models.CharField(null=True,blank=True,verbose_name='Profesión u Oficio',max_length=200)

    class Meta:
        ordering =['user__username']
    

#definir señales- señal para que al registrarse un usuario se cree un perfil
@receiver(post_save, sender= User)
def ensure_profile_exist(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user= instance)
        #print("se acaba de crear un usuario y su perfil enlazado")