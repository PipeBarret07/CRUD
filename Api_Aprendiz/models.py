from django.db import models

class Aprendices(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    año = models.DateField(max_length=10)
    documento = models.IntegerField()
    tipo_de_documento = models.CharField(max_length=10)
    numero_de_ficha = models.PositiveIntegerField()
    
