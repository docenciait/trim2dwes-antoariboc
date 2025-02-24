from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORIAS = ['1','2','3']

class Denuncia (models.Model):
    
    BACHE = 'bache'
    ALUMBRADO = 'alumbrado'
    BASURA = 'basura'
    OTRO = 'otro'
    CATEGORIAS = [
    (BACHE, ('bache')),
    (ALUMBRADO, ('alumbrado')),
    (BASURA, ('basura')),
    (OTRO, ('otro')),
    ]  
    
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    image = models.ImageField()
    categoria = models.CharField(max_length=20,choices=CATEGORIAS,default=OTRO)
    estado = models.CharField(default='pendiente', max_length=20)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario= models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo + ' - ' + self.estado
