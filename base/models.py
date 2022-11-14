from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Alumno(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    

class Nota(models.Model):
    alumno = models.OneToOneField(Alumno, on_delete=models.CASCADE, primary_key=True)
    nota = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.alumno.nombre}: {self.nota}'
