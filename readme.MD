# Primer paso instalar Django a nivel global - optativo
python3 -m pip install Django

# Segundo paso crear nuevo proyecto:
python3 -m django startproject mi_primer_proyecto

# Instalo en entorno virtual venv
python3 -m venv venv

# Creo el archivo requirements.txt
pip3 freeze > requirements.txt
pip3 install -r requirements.txt

# Creo mi app
python3 manage.py startapp mi_app
aparece una carpeta nueva en el proyecto

# A esa carpeta mi_app le creo un archivo urls.py
Para eso copio y pego el urls de la otra carpeta Django_project
Cambio 

# Cada vez que creo un nuevo class en models.py
python3 manage.py makemigrations
python3 manage.py migrate

# Si hay errores al intentar migrar
borrar todo de la carpeta migrations excepto __init.py__
borrar la db
y volver a hacer el paso anterior

# Para ejecutar el servidor
python3 manage.py runserver

