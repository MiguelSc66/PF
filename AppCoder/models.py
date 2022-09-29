from django.db import models

# Create your models here.
class Family3(models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    fechaNac = models.DateField()

class estudiate(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    correo = models.EmailField()
    
class profesor(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    correo = models.EmailField()
    profesion = models.CharField(max_length=60)

class entregable(models.Model):
    nombre = models.CharField(max_length=60)
    fechaDeEntrega = models.DateField()

