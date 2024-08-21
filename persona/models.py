from django.db import models

class TipoPersona(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class Persona(models.Model):
    tipo_persona = models.ForeignKey(TipoPersona, on_delete=models.CASCADE)
    apellidos = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.apellidos}, {self.nombres}"
