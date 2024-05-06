from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(User):
    TIPO_USUARIO_CHOISES = [
        ('arrendatario', 'Arrendatario'),
        ('arrendador', 'Arrendador'),
    ]
    nombres=models.CharField(max_length=50, null=False, blank=False)
    apellidos=models.CharField(max_length=50, null=False, blank=False)
    rut=models.CharField(max_length=10,unique=True)
    direccion=models.CharField(max_length=100)
    telefono=models.CharField(max_length=13)
    tipo_usuario=models.CharField(max_length=20,choices=TIPO_USUARIO_CHOISES)
    correo_electronico=models.EmailField(unique=True, default='correo@correo.cl')
        
    def __str__(self):
        return f"{self.nombres} {self.apellidos}" 

class Inmueble(models.Model):
    TIPO_INMUEBLE_CHOISES = [
        ('casa', 'Casa'),
        ('departamento', 'Departamento'),
        ('parcela', 'Parcela'),
    ]    
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='')
    precio=models.DecimalField(max_digits=10, decimal_places=0)
    comuna=models.CharField(max_length=50)
    disponible=models.BooleanField(default=True)
    m2_construidos=models.DecimalField(max_digits=10, decimal_places=2)
    m2_terreno=models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_de_estacionamientos=models.PositiveIntegerField()
    cantidad_de_habitaciones=models.PositiveIntegerField()
    cantidad_banos=models.PositiveIntegerField()
    tipo_de_inmueble=models.CharField(max_length=12,choices=TIPO_INMUEBLE_CHOISES)
    propietario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.nombre}"
    
class SolicitudArriendo(models.Model):
    arrendatario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    inmueble=models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    mensaje=models.TextField(blank=True)
    
    def __str__(self) -> str:
        return f"Solicitud de {self.inmueble.nombre} por {self.arrendatario.nombres} {self.arrendatario.apellidos}"