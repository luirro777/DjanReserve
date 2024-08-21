from django.db import models

class TipoLugar(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class Lugar(models.Model):
    tipo_lugar = models.ForeignKey(TipoLugar, on_delete=models.CASCADE)
    numero = models.CharField(max_length=10)
    disponible_ahora = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.tipo_lugar.descripcion} - {self.numero}"
