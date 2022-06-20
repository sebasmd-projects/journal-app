# Django

Qué es [Django]:\
Django es un Framework web Python de alto nivel que fomenta un desarrollo rápido y un diseño limpio y pragmático. Creado por desarrolladores experimentados, se encarga de gran parte de las molestias del desarrollo web, por lo que puede concentrarse en escribir su aplicación sin necesidad de reinventar la rueda. Es gratis y de código abierto.

## Comandos útiles
En el directorio del proyecto (a la altura del manage.py) puedes ejecutar:

> Nota:\
En linux y mac utilizar `python3`

### `runserver`
Levantar servidor local en el puerto :8000 por defecto
abrir `localhost:8000` o `127.0.0.1:8000` en el navegador
```sh
python manage.py runserver
```

### `makemigrations`
Se encarga de crear las nuevas migraciones en función de los cambios que se hayan realizado en los modelos
```sh
python manage.py makemigrations
```

### `migrate`
Se encarga de aplicar, remover o cambiar de migración en la base de datos
```sh
python manage.py migrate
```

### `createsuperuser`
Crear usuario con permisos administrativos y con acceso al administrador de Django
```sh
python manage.py createsuperuser
```

### ```startproject```
Crear un nuevo proyecto de Django
```sh
django-admin startproject nombre_del_proyecto .
```

### ```startapp```
Dentro de la carpeta apps o applications, crear una nueva aplicación de Django.
>Nota:\
Recordar que si la aplicación no se crea dentro de la carpeta ppal hay que modificar el settings con `apps.nombre_de_la_app` y dentro de la aplicación el archivo apps.py añadir `apps.` quedando apps.nombre_de_la_app
```sh
cd apps
django-admin startapp nombre_de_la_app
```

### ```loaddata```
Utilizar una copia de los datos de una base de datos
```sh
python manage.py loaddata
```

### ```dumpdata ```
Realizar una copia de la base de datos
```sh
python manage.py dumpdata
```

### ```inspectdb ```
Copiar las tables de 
```sh
python manage.py dumpdata
```

### ```migrate app_name zero```
Para borrar una migración de una clase model.Model
Borrar las migraciones de la carpeta migrations
```sh
python manage.py migrate app_name zero
```


>Nota:\
En la configuración de correo utilizat EMAIL_USE_SSL = True con el puerto 465 y EMAIL_USE_TLS = True si el puerto es el 587

[Django]: https://www.djangoproject.com/start/overview/
