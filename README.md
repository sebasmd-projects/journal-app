# Journal APP
## Requerimientos
Desarrollar una aplicación web para registrar los diarios de campo de las clases dictadas por los docentes de la institución INEM cada registro debe contener los siguientes items o campos:
1. Nombre de los docentes
2. Nombre de las asignaturas
3. Temas
4. Fechas
5. Reflexión pedagógica
6. Descripción
7. Sección

Tablas requeridas en el modelado de la BD
1. Docentes
2. Temarios
3. Diario de Campo

Nota:\
La aplicación debe mostrar que temas se han dictado y cuales estan pendientes por asignatura y sección

## Historias de usuario
1. Registrar Docentes
2. Iniciar sesión
3. Registrar diario de Campo
4. Poder consultar temas dictados por asignatura y sección
5. Poder consultas temas pendientes por asignatura y sección
6. Realizar informes del Diario de Campo

## Ejemplo:
### **Docente:** Pepito Perez
#### **Materia o Curso:** Fundamentos de Invesitgación
#### **Secciones:** 7,8,9

> **Fecha:** Febrero 18 de 2022\
> **Tema:** Estado del arte\
> **Descripción del tema:** \
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus suscipit tortor eget felis porttitor volutpat. Nulla porttitor accumsan tincidunt.\
Cras ultricies ligula sed magna dictum porta. Cras ultricies ligula sed magna dictum porta. Curabitur aliquet quam id dui posuere blandit.\
> **Reflexión Pedagógica:**\
Proin eget tortor risus. Quisque velit nisi, pretium ut lacinia in, elementum id enim. Nulla porttitor accumsan tincidunt.
---
> **Fecha:** Febrero 21 de 2022\
> **Temas:** Tipos de investigación\
> **Descripción del tema:**\
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus suscipit tortor eget felis porttitor volutpat. Nulla porttitor accumsan tincidunt.\
Cras ultricies ligula sed magna dictum porta. Cras ultricies ligula sed magna dictum porta. Curabitur aliquet quam id dui posuere blandit.\
> **Reflexión Pedagógica:**\
Proin eget tortor risus. Quisque velit nisi, pretium ut lacinia in, elementum id enim. Nulla porttitor accumsan tincidunt.

## Jounral APP
Journal APP es una proyecto pensado para manejar de manera sencilla los diarios de campo
- Backend: [Django] v4.0.5 | Sistema de plantillas (HTML) con Bootstrap (SB Admin Pro - Solo HTML y CSS)
- Frontend: [React] v18.1.0 | SB Admin PRO - License: Developer

### Pre-requisitos
- [Python3]
- [Node]
- [Git] y Github
- [PostgreSQL] u otra base de datos

#### Tecnologías de Django
- [Vistas basadas en clase]
- [Django Rest Framework]

#### Tecnologías de React
- [React Dom] v18.1.0

## Iniciar Django
1. Ir al archivo sensitive_data.json
2. Dependiendo del entorno (Local, Producción, Desarrollo), cambiar "ENVIRONMENT" por "dev", "local" o "production"
3. Cambiar la url base al dominio propio
4. Añadir una secret key
5. Configurar el lenguaje al local
6. Actualizar la zona horaria
7. Añadir los dominios permitidos de la aplicación
8. Añadir los dominios de terceros
9. Configurar el proveedor de correo
10. Configurar la base de datos | instalar su paquete correspondiente ejm:
    - Windows: `pip install psycopg2`
    - Linux: `pip install psycopg2-binary`

Algunos ejemplos para configurar la BD
> **Sqlite:**\
'ENGINE': 'django.db.backends.sqlite3',\
'NAME': BASE_DIR.child('nombre_de_la_db.sqlite3')

> **Postgresql:**\
'ENGINE': 'django.db.backends.postgresql_psycopg2'\
'NAME': 'nombre_de_la_bd',\
'USER': 'usuario_asociado_a_la_db',\
'PASSWORD': 'contraseña_del_usuario',\
'HOST': 'localhost',\
'PORT': '5432'

> **MariaDB o MySQL**\
'ENGINE': 'django.db.backends.mysql',\
'NAME': 'nombre_de_la_bd', \
'USER': 'usuario_asociado_a_la_db', \
'PASSWORD': 'contraseña_del_usuario', \
'HOST': 'localhost', \
'PORT': '3306'

Para linux o mac utilizar `python3`

Crear el entorno virtual y activarlo | **WINDOWS**
```sh
python -m venv venv_nombreDelEntorno
cd venv_nombreDelEntorno
Scripts\activate
```

Crear el entorno virtual y activarlo | **LINUX**
```sh
python3 -m venv venv_nombreDelEntorno
source venv_nombreDelEntorno\bin\activate
```

Ir a la carpeta documentation\requirements y dependiendo de tu entorno y terminal (CMD en windows, WSL, Powershell, etc) realizar la instalación de librerias
```sh
pip install -r local_windows_requirements.txt
```

A la altura del manage.py y con el entorno activo

```sh
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Iniciar React
1.
2.
3.
4.

```sh
cd Frontend
npm start
```

## Extra Versionamiento | Git y Github
* Iniciar Git
```sh
git init
```
* Si no se ha configurado git
Asignar un usuario global y correo
```sh
git config --global user.name "Nombre de Usuario"
git config --global user.email "ejemplo@correo.com"
```

* Para evitar que salga el error\
"warning: LF will be replaced by CRLF in Frontend/src/setupTests.js.
The file will have its original line endings in your working directory"
```sh
git config core.autocrlf true
```

* Crear una nueva rama
```sh
git branch NombreDeLaRama
```

* Borrar una rama
```sh
git branch -d NombreDeLaRama
```

* Status\
**-s** Ver solo los archivos con cambios\
**-b** Ver la rama en la que se esta trabajando
```sh
git status -s
git status -b
```

* Añadir los cambios\
Con el `git add .` Añadimos todos los cambios
```sh
git add .
git add nombre_archivo.formato
git add *.formato
git add carpeta/
git add carpeta/*.formato
```

* Crear un commit
```sh
git commit -m "mensaje en presente con los cambios"
```

* Corregir un commit
```sh
git commit --amend -m "Mensaje en presente con los cambios"
git commit -am "Mensaje en presente con los cambios"
```

* Regresar al último commit
```sh
git checkout -- .
```

* Ver todos los commits
```sh
git log --decorate
git log --graph
git log --all
```

* Cambiar de rama\
`checkout -b` para crear y moverse a esa rama
```sh
git checkout NombreDeLaRama
git checkout -b NombreDeLaRama
```

* Unir ramas\
Estando en la rama principal
```sh
git merge NombreDeLaRamaSecundaria
```

* Crear tags
```sh
git tag -a NombreDelTag -m "Mensaje del tag"
git tag -a NombreDelTag HASH -m "Mensaje del tag con commit"
```

* Añadir a Github | Primer push caso contrario usar merge
```sh
git remote add origin URL
git branch -M NombreDeLaRama
git push -u origin NombreDeLaRama
git push --tags
```

* "Extraer" de Github
```sh
git pull
```

git commit -m "Se crea el proyecto de Django en la v4.0.5 y de React en la versión 18.1.0 | Se crean las aplicaciones de Django auth, home y journal | Se crea la estrucura de carpetas en Django | Se reestructura el settings.py | 

[Django]: https://docs.djangoproject.com/en/4.0/
[React]: https://github.com/facebook/react/blob/main/CHANGELOG.md#1810-april-26-2022
[PostgreSQL]: https://www.postgresql.org/download/
[Vistas basadas en clase]: https://ccbv.co.uk/
[Django Rest Framework]: https://www.django-rest-framework.org/
[React Dom]: https://www.npmjs.com/package/react-dom
[Python3]: https://www.python.org/downloads/
[Node]: https://nodejs.org/es/download/
[Git]: https://git-scm.com/downloads