import os
from gen.helpers.helper_print import print_message, GREEN, CYAN

def generate_readme(full_path, project_name):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path)
    file_path = os.path.join(folder_path, "readme.md")

    os.makedirs(folder_path, exist_ok=True)

    content = r'''## {project_name}

## Script para ejecutar el proyecto

```sh
python3 manage.py check                         # Chequear dependencias
python3 manage.py makemigrations                # Migraciones
python3 manage.py migrate                       # Aplicar migraciones
python manage.py collectstatic --noinput        # Recopilar archivos estaticos
python3 manage.py seed_user                     # Crear superuser
python3 manage.py seed_default                  # Crear Prompts
python3 manage.py runserver                     # Ejecutar servidor
```

## Crear entorno virtual

```sh
## Entorno virtual MacOs
- python3 -m venv .venv
- source .venv/bin/activate                     # Activar entorno
- deactive                                      # Desactivar entorno                               # Usar este comando para intrucciones

## Actualizar PIP
pip install --upgrade pip


## Instala los requerimientos:
pip freeze > requirements.txt                  # Crear archivo requerimientos -> Respaldo / Export
pip install -r requirements.txt                # Instalar requerimientos Restore / Import

## Si No se tiene el archivo: requirements.txt
pip install pipreqs                             # Install
pipreqs . --force                               # Ejecutar


## Instalar paquetes
pip freeze                                     # Ver Paquetes instalados
py -m pip freeze                                # Para Windows
pip install requests                           # Conexion API
pip install schedule                           # CronJobs


## Si no funciona VSCode:
( Cmd + Shift + P ) -> luego "Python: Select Interpreter" elegir ".venv/bin/python"
```


## Commands

```sh
python3 manage.py seed_user                     # Crear superuser
python3 manage.py createsuperuser               # Consola Crear superuser

python3 manage.py clear_migrations --dry-run     # Muestra las migraciones
python3 manage.py clear_migrations               # Elimina las migraciones

```


## Docker

```sh

## levantar con Docker:
docker compose up -d

## Opcional:
docker compose down -v                          ## Borra la BD
docker compose up -d                            ## Se levanta de nuevo

```



## Libraries

```sh
pip install pdfkit                              # Crear PDF
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

python3 manage.py seed_user                             # Seeder
python3 manage.py createsuperuser                       # Consola Crear superuser

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
    chown -R xxx:pppp /var/www/vhosts/x.com/api.x.com
    find /var/www/vhosts/x.com/api.x.com -type d -exec chmod 755 {} \;
    find /var/www/vhosts/x.com/api.x.com -type f -exec chmod 644 {} \;
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

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)