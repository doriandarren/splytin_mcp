from gen.helpers.helper_file import HelperFile


class PyGenerateReadme:
    
    
    def invoke(self, full_path, project_name, project_name_format, domain_name):
        """
        Genera el archivo readme.md.
        """

        content = r'''# Project __PROJECT_NAME__
                
## Script para ejecutar el proyecto

```sh
## Crear el entorno - Venv
python3 -m venv .venv
source .venv/bin/activate 
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Crear raíz del proyecto: 
- Archivo .env -> chmod 600 /var/www/vhosts/__DOMAIN_NAME__/__PROJECT_NAME__/.env
- Carpeta logs
- Carpeta media

# Django
python manage.py check                         # Chequear dependencias
python manage.py makemigrations                # Migraciones
python manage.py migrate                       # Aplicar migraciones
python manage.py collectstatic --noinput        # Recopilar archivos estaticos
python manage.py seed_users                    # Crear superuser
python manage.py runserver                     # Ejecutar servidor
```


## Crear entorno virtual Venv

```sh
## Instala los requerimientos:
python -m pip freeze > requirements.txt          # Crear archivo requerimientos -> Respaldo / Export
python -m pip install -r requirements.txt        # Instalar requerimientos Restore / Import

## Si no se tiene el archivo: requirements.txt
python -m pip install pipreqs                    # Install
pipreqs . --force                                # Ejecutar

## Instalar paquetes
python -m pip freeze                            # Ver Paquetes instalados

## Si no funciona VSCode:
(Cmd + Shift + P) -> luego "Python: Select Interpreter" elegir ".venv/bin/python"
```


## Commands

```sh
python3 manage.py seed_user                      # Crear superuser
python3 manage.py createsuperuser                # Consola Crear superuser

python3 manage.py clear_migrations --dry-run     # Muestra las migraciones
python3 manage.py clear_migrations               # Elimina las migraciones

```


## Docker

```sh
docker compose up -d                            ## levantar con Docker
docker compose down -v                          ## Borra la BD
docker compose up -d                            ## Se levanta de nuevo
```


## Packages / Libraries 

```sh
python -m pip install pdfkit                    # Crear PDF
python -m pip install requests                  # Conexion API
python -m pip install schedule                  # CronJobs
```


## Django

```sh

## BY PROJECT
django-admin startproject nombre_proyecto       # Crear PROJECT
django-admin startproject nombre_proyecto .     # Crear PROJECT - No crea carpeta duplicada

## BY APP
python3 manage.py startapp nombre_app           # Crear app

python manage.py migrate
python3 manage.py runserver                     # Levantar el servidor
python3 manage.py runserver 8001
python3 manage.py seed_user                     # Seeder
python3 manage.py createsuperuser               # Consola Crear superuser
```

## Django + Celery + Beat + Redis

```sh
# importante instalar Redis y tenerlo corriendo en el puerto 6379

celery -A celery_app worker -l info
celery -A celery_app beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
python manage.py runserver

# Dar permisos:
chmod +x start_celery.sh

# Arrancar:
./start_delery.sh

# Logs:
cat logs/django.log
cat logs/celery_worker.log
cat logs/celery_beat.log

```

## Error: python manage.py makemigrations

```sh

## Error cuando se agrega el created_at al modelo:
opc: 1
>>> timezone.now()

```

## By Plesk:

```sh

- Entorno virtual para el proyecto
- Modificar ENV: cp .env.example .env
- Ejecutar comandos readme.md - Script para iniciar el proyecto
- Cambiar permisos:
    chown -R xxx:pppp /var/www/vhosts/__DOMAIN_NAME__/__PROJECT_NAME_FORMAT__
    find /var/www/vhosts/__DOMAIN_NAME__/__PROJECT_NAME_FORMAT__ -type d -exec chmod 755 {} \;
    find /var/www/vhosts/__DOMAIN_NAME__/__PROJECT_NAME_FORMAT__ -type f -exec chmod 644 {} \;
    chmod +x manage.py
    chmod +x start_celery.sh
    chmod -R 775 logs
    chmod -R 775 tmp

- Conectar DB:
    * Base datos SQLte: chmod 666 db.sqlite3
    * Base datos PostgreSQL

## Reiniciar app con Passenger
touch tmp/restart.txt

```
'''

        # Reemplazar variables
        content = content.replace("__PROJECT_NAME__", project_name)
        content = content.replace(
            "__PROJECT_NAME_FORMAT__",
            project_name_format
        )
        content = content.replace("__DOMAIN_NAME__", domain_name)

        # Crear el archivo
        HelperFile.write(
            folder_path=full_path,
            file_name="readme.md",
            content=content
        )