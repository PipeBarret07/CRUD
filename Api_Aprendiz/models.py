from django.db import models

class  Aprendices(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.URLField(max_length=100)
    fecha_de_nacimiento = models.DateField()
    documento = models.
    tipo_de_docuento =
    numero_de_ficha = 
    
