from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Perfil(models.Model):
    #Informacion Genral
    DNI = models.IntegerField(primary_key=True,blank = False,unique = True)
    usuario = models.OneToOneField(User, related_name="profile_user")
    GENEROS = (
    ('M', 'Masculino'),
    ('F', 'Femenino')
    )
    genero = models.CharField(max_length=30, choices= GENEROS, default='M')
    nacimiento = models.DateField(default = '1985-01-01')
    foto = models.ImageField (blank=False)

    # Direccion del Usuario
    direccion = models.CharField (max_length= 150, blank = True)
    lat = models.CharField(max_length = 50, blank = True)
    lng = models.CharField(max_length = 50, blank = True)
    #contacto
    celular = models.IntegerField(null=True,blank = True)
    telefono = models.IntegerField(null=True,blank = True)
    trabajo = models.IntegerField(null=True,blank = True)
    referencia = models.CharField(max_length = 80,blank = True)



    agencia = models.ForeignKey(Agencia, blank=False)
    ESTADOS = (
    ('ACTIVO', 'Activo'),
    ('BAJA', 'Baja'),
    ('BAJATEMP', 'Baja Temporal')
    )
    estado = models.CharField(max_length=15, choices= ESTADOS)

    #datos afps
    AFPS = (
    ('FUTURO', 'Futuro'),
    ('PREVISION', 'Prevision')
    )
    #datos solo para RRHH
    afp = models.CharField(max_length=15, choices= AFPS, blank = True)
    nua = models.CharField(max_length = 20,blank = True)
    numero_afiliacion = models.CharField(max_length = 20,blank = True)

    persona_ref1 = models.CharField(max_length=50,blank=True,unique = False)
    telefono_ref1 = models.IntegerField(null=True,blank = True)

    persona_ref2 = models.CharField(max_length=50,blank=True,unique = False)
    telefono_ref2 = models.IntegerField(null=True,blank = True)

    user = models.ForeignKey(User)
    fecha_creacion = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return str(self.usuario)
