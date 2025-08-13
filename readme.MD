

**Aplicación de Agenda**
=====================

Una aplicación de agenda integral construida con Django, que incluye gestión de contactos, tareas y notas.
La aplicacion incluye registo, login y logout de usuarios.

**Descripción general**
--------------------

La Aplicación de Agenda es una aplicación web construida con Django, diseñada para ayudar a los usuarios a gestionar sus contactos, tareas y notas en una sola plataforma. La aplicación proporciona una interfaz limpia y intuitiva, lo que facilita la organización y priorización de tareas, el almacenamiento de información de contacto importante y la toma de notas, al igual que el agregado de tareas a realizar.

**Características**
-----------------

* **Gestión de contactos**:
	+ Crear, buscar y listar contactos
	+ Almacenar información de contacto, incluyendo nombre, apellido y correo electrónico
	+ Buscar y filtrar contactos por nombre.
* **Gestión de tareas**:
	+ Crear y listar tareas
	+ Marcar tareas como completadas
* **Gestión de notas**:
	+ Crear, editar, eliminar y listar notas
	+ Almacenar notas con títulos, contenido y estado

**Instalación**
------------

Para instalar la Aplicación de Agenda, sigue estos pasos:

1. Clona el repositorio: `git clone https://github.com/LauGM/Proyecto-agenda-django`
2. Crea un entorno virtual: `python -m venv venv`
3. Activa el entorno virtual: `source venv/bin/activate` (en Linux/Mac) o `venv\Scripts\activate` (en Windows)
4. Instala dependencias: `pip install -r requirements.txt`
5. Ejecuta migraciones: `python manage.py migrate`
6. Crea un superusuario: `python manage.py createsuperuser`

**Uso**
-----

1. Ejecuta el servidor de desarrollo: `python manage.py runserver`
2. Accede a la aplicación en tu navegador web: `http://localhost:8000`
4. Explora las características y funcionalidades de la aplicación

**Esquema de base de datos**
-------------------------

La Aplicación de Agenda utiliza una base de datos SQLite. El esquema de la base de datos se define en el archivo `models.py` e incluye las siguientes tablas:

* `contactos`
* `tareas`
* `notas`


**Colaboración**
--------------

Las contribuciones son bienvenidas. Si deseas colaborar en la Aplicación de Agenda, por favor bifurca el repositorio y envía una solicitud de extracción.

**Licencia**
---------

La Aplicación de Agenda está licenciada bajo la Licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.

**Pre-deploy**
---------
[Link a Render.com](https://proyecto-agenda-django.onrender.com/)

## Laura González Martin