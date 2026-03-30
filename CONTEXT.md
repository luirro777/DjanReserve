# Contexto del Proyecto - Sistema de Reservas Django

## Descripción General

Aplicación web Django para gestión de reservas de espacios/lugares. Permite administrar personas, lugares y reservas (agendas) con validación de horarios para evitar conflictos.

## Estructura del Proyecto

```
djanreserve/
├── djanreserve/                  # Paquete principal del proyecto
│   ├── reserva/                  # Configuración Django (settings, urls, wsgi)
│   ├── persona/                  # App: Gestión de personas
│   ├── lugar/                    # App: Gestión de lugares/tipos de lugar
│   ├── agenda/                   # App: Gestión de reservas
│   ├── templates/                # Templates base y parciales
│   └── manage.py                 # Script de gestión Django
```

## Aplicaciones

### Persona
- **Modelos**: `Persona`, `TipoPersona`
- **Campos**: tipo_persona (FK), apellidos, nombres
- **Views**: CRUD completo con ListView, DetailView, CreateView, UpdateView, DeleteView

### Lugar
- **Modelos**: `Lugar`, `TipoLugar`
- **Campos**: tipo_lugar (FK), numero, disponible_ahora
- **Views**: CRUD completo con ListView, DetailView, CreateView, UpdateView, DeleteView

### Agenda (Reservas)
- **Modelo**: `Agenda`
- **Campos**: titulo, descripcion, persona (FK), lugar (FK), fecha, hora_comienzo, hora_final
- **Validaciones**: 
  - Hora de comienzo < hora final
  - No permitir reservas solapadas en mismo lugar
- **Views**: CRUD completo + vista de próximas reservas por lugar

## Configuración Actual

- **DEBUG**: True
- **Database**: SQLite (db.sqlite3)
- **Static**: /static/
- **Time Zone**: UTC
- **Language**: en-us

## URLs

- `/admin/` - Panel de administración
- `/personas/` - Gestión de personas
- `/lugares/` - Gestión de lugares
- `/agendas/` - Gestión de reservas

## Tecnologías

- Django 4.2
- Python 3.x
- Bootstrap 5.3 (frontend)
- SQLite (desarrollo)

## Variables de Entorno Requeridas

- `SECRET_KEY`: Clave secreta de Django
- `DEBUG`: True/False
- `ALLOWED_HOSTS`: Hosts permitidos (separados por coma)
- `DATABASE_URL`: URL de conexión a PostgreSQL (producción)
- `POSTGRES_DB`: Nombre de base de datos
- `POSTGRES_USER`: Usuario PostgreSQL
- `POSTGRES_PASSWORD`: Contraseña PostgreSQL
