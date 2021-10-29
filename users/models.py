from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import datetime

class MyAccountManager(BaseUserManager):

    def __init__(self) -> None:
         super().__init__()

    #Permite la creación de usuario con los campos adicionados
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Falta email')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_staff', True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    #Permite la creación de superusuario
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        user = self.create_user(email, password, **extra_fields)
        return user

#AbstractUser para agregar los campos descritos en la prueba
class CustomUser(AbstractUser):
    
    class Meta:
        db_table = 'Users'
    
    #Datos de administración
    is_active =  models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    email = models.EmailField(verbose_name="email", unique=True, default="")
    date_joined = models.DateTimeField(auto_now_add=True)

    #Campos requeridos por la prueba
    username = models.CharField(max_length=40, unique=False, default='')
    nombre = models.CharField(max_length=100, default="")
    apellido_uno = models.CharField(max_length=50, default="")
    apellido_dos = models.CharField(max_length=50, default="")
    cedula = models.CharField(max_length=20, unique=True, default="")
    fecha_nacimiento = models.DateField(default=datetime.date.today)
    genero = models.CharField(max_length=1, default="")
    fecha_ingreso =  models.DateField(default=datetime.date.today)
    numero_empleado = models.IntegerField(unique=True, default=0)
    cargo = models.CharField(max_length=25, default="")
    jefe = models.IntegerField(default=0)
    zona = models.CharField(max_length=20, default="")
    municipio = models.CharField(max_length=20, default="")
    departamento = models.CharField(max_length=20, default="")
    ventas = models.IntegerField(default=0)
    imagen = models.CharField(max_length=255, null=True, blank=True, default="")
    celular = models.CharField(max_length=20, default="")

    #Se cambia el username por el email para loguear
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyAccountManager()