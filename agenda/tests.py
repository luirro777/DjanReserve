from django.test import TestCase
from django.urls import reverse
from .models import Agenda
from persona.models import Persona, TipoPersona  # Asegúrate de importar TipoPersona
from lugar.models import Lugar, TipoLugar  # Asegúrate de importar TipoLugar
from datetime import date, time

class AgendaViewsTest(TestCase):

    def setUp(self):
        self.tipo_persona = TipoPersona.objects.create(descripcion='Cliente')
        self.persona = Persona.objects.create(tipo_persona=self.tipo_persona, apellidos='González', nombres='Juan')
        self.tipo_lugar = TipoLugar.objects.create(descripcion='Sala de reuniones')
        self.lugar = Lugar.objects.create(tipo_lugar=self.tipo_lugar, numero='101', disponible_ahora=True)
        self.agenda = Agenda.objects.create(
            persona=self.persona,
            lugar=self.lugar,
            fecha=date(2024, 8, 21),
            hora_comienzo=time(10, 0),
            hora_final=time(12, 0)
        )

    def test_agenda_list_view(self):
        response = self.client.get(reverse('agenda_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.agenda.persona.nombres)
        #self.assertTemplateUsed(response, 'agenda/agenda_list.html')  # Si usas templates, sino omite esta línea

    def test_agenda_detail_view(self):
        response = self.client.get(reverse('agenda_detail', args=[self.agenda.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.agenda.lugar.numero)

    def test_agenda_create_view(self):
        response = self.client.post(reverse('agenda_create'), {
            'persona': self.persona.id,
            'lugar': self.lugar.id,
            'fecha': '2024-08-22',
            'hora_comienzo': '14:00:00',
            'hora_final': '16:00:00'
        })
        self.assertEqual(response.status_code, 302)  # Redirección tras éxito
        self.assertTrue(Agenda.objects.filter(fecha='2024-08-22').exists())

    def test_agenda_update_view(self):
        response = self.client.post(reverse('agenda_update', args=[self.agenda.id]), {
            'persona': self.persona.id,
            'lugar': self.lugar.id,
            'fecha': '2024-08-23',
            'hora_comienzo': '10:00:00',
            'hora_final': '12:00:00'
        })
        self.assertEqual(response.status_code, 302)  # Redirección tras éxito
        self.agenda.refresh_from_db()
        self.assertEqual(self.agenda.fecha, date(2024, 8, 23))

    def test_agenda_delete_view(self):
        response = self.client.post(reverse('agenda_delete', args=[self.agenda.id]))
        self.assertEqual(response.status_code, 302)  # Redirección tras éxito
        self.assertFalse(Agenda.objects.filter(id=self.agenda.id).exists())
