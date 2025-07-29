

**Aplicación de Agenda**
=====================

Una aplicación de agenda integral construida con Django, que incluye gestión de contactos, tareas y notas.

**Índice**
----------

1. [Descripción general](#descripcion-general)
2. [Características](#caracteristicas)
3. [Instalación](#instalacion)
4. [Uso](#uso)
5. [Esquema de base de datos](#esquema-de-base-de-datos)
6. [Documentación de la API](#documentacion-de-la-api)
7. [Colaboración](#colaboracion)
8. [Licencia](#licencia)

**Descripción general**
--------------------

La Aplicación de Agenda es una aplicación web construida con Django, diseñada para ayudar a los usuarios a gestionar sus contactos, tareas y notas en una sola plataforma. La aplicación proporciona una interfaz limpia y intuitiva, lo que facilita la organización y priorización de tareas, el almacenamiento de información de contacto importante y la toma de notas.

**Características**
-----------------

* **Gestión de contactos**:
	+ Crear, editar y eliminar contactos
	+ Almacenar información de contacto, incluyendo nombre, correo electrónico, número de teléfono y dirección
	+ Buscar y filtrar contactos por nombre, correo electrónico o número de teléfono
* **Gestión de tareas**:
	+ Crear, editar y eliminar tareas
	+ Asignar tareas a contactos específicos
	+ Establecer fechas de vencimiento y recordatorios para tareas
	+ Marcar tareas como completadas
* **Gestión de notas**:
	+ Crear, editar y eliminar notas
	+ Almacenar notas con títulos, contenido y etiquetas
	+ Buscar y filtrar notas por título, contenido o etiquetas
* **Autenticación de usuarios**:
	+ Registro y inicio de sesión de usuarios
	+ Restablecimiento de contraseña y verificación de correo electrónico

**Instalación**
------------

Para instalar la Aplicación de Agenda, sigue estos pasos:

1. Clona el repositorio: `git clone https://github.com/tu-usuario/agenda-app.git`
2. Crea un entorno virtual: `python -m venv venv`
3. Activa el entorno virtual: `source venv/bin/activate` (en Linux/Mac) o `venv\Scripts\activate` (en Windows)
4. Instala dependencias: `pip install -r requirements.txt`
5. Ejecuta migraciones: `python manage.py migrate`
6. Crea un superusuario: `python manage.py createsuperuser`

**Uso**
-----

1. Ejecuta el servidor de desarrollo: `python manage.py runserver`
2. Accede a la aplicación en tu navegador web: `http://localhost:8000`
3. Inicia sesión con tus credenciales de superusuario
4. Explora las características y funcionalidades de la aplicación

**Esquema de base de datos**
-------------------------

La Aplicación de Agenda utiliza una base de datos PostgreSQL. El esquema de la base de datos se define en el archivo `models.py` e incluye las siguientes tablas:

* `contactos`
* `tareas`
* `notas`
* `usuarios`

**Documentación de la API**
-------------------------

La Aplicación de Agenda proporciona una API RESTful para interactuar con los datos de la aplicación. La documentación de la API está disponible en `http://localhost:8000/api/docs`.

**Colaboración**
--------------

Las contribuciones son bienvenidas. Si deseas colaborar en la Aplicación de Agenda, por favor bifurca el repositorio y envía una solicitud de extracción.

**Licencia**
---------

La Aplicación de Agenda está licenciada bajo la Licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.