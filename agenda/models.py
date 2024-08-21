from django.db import models
from persona.models import Persona
from lugar.models import Lugar

class Agenda(models.Model):
    titulo = models.CharField("Titulo", max_length=50)
    descripcion = models.TextField()
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora_comienzo = models.TimeField()
    hora_final = models.TimeField()

    def __str__(self):
        return f"Agenda de {self.persona} en {self.lugar} el {self.fecha} de {self.hora_comienzo} a {self.hora_final}"
    
    def clean(self):
        if self.hora_comienzo >= self.hora_final:
            raise ValidationError('La hora de comienzo debe ser anterior a la hora final.')

    class Meta:
        unique_together = ('lugar', 'fecha', 'hora_comienzo', 'hora_final')
