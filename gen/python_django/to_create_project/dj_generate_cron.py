import os
from gen.helpers.helper_print import print_message, GREEN, CYAN, run_command
from gen.python_django.helpers.helper_file import helper_append_content, helper_update_list
from gen.helpers.helper_file import HelperFile



class DjGenerateCron:

    def invoke(self, full_path, project_name_format, app_main, venv_python):
        """
        Genera el archivo
        """    
        self.install_cron(full_path, venv_python)
        self.update_settings(full_path, app_main)
        self.create_file_init(full_path)
        self.create_file_celery(full_path, app_main)
        self.create_file_cron_devs(full_path)
        self.create_file_sh(full_path)



    def install_cron(self, full_path, venv_python):
        print_message("Instalando Celery...", CYAN)
        run_command(f'"{venv_python}" -m pip install celery django-celery-beat redis', cwd=full_path)
        print_message("Celery instalado correctamente.", GREEN)
        
        
    
    def update_settings(self, full_path, app_main):
        
        helper_update_list(
            full_path, 
            f"{app_main}/settings.py", 
            "INSTALLED_APPS", 
            f"'django_celery_beat',                           # required for celery beat"
        )    
        
        
        str = r"""# Celery
CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
CELERY_TIMEZONE = "Europe/Madrid"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"

# Celery Beat Schedule
# CELERY_BEAT_SCHEDULE = {
#     "hello-every-minute": {
#         "task": "apps.devs.tasks.start",
#         "schedule": crontab(minute="*"),
#     },
#     "hello-every-5-minutes": {
#         "task": "apps.devs.tasks.start",
#         "schedule": crontab(minute="*/5"),
#     },
# }
    """
        
        helper_append_content(
            full_path, 
            f"{app_main}/settings.py", 
            str
        )
        
    
    
    def create_file_init(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "celery_app")

        content = f'''from .celery import app

__all__ = ("app",)
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="__init__.py",
            content=content
        )
    
    
    def create_file_celery(self, full_path, app_main):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "celery_app")

        content = f'''import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{app_main}.settings")

app = Celery("{app_main}")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="celery.py",
            content=content
        )
        
    
    def create_file_cron_devs(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "apps", "devs")

        content = r'''from celery import shared_task
from django.utils import timezone


@shared_task
def start():
    now = timezone.now()
    print(f"Hola desde Celery: {now}")
    return f"Ejecutado en {now}"
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="tasks.py",
            content=content
        )
    
    
    
    
    def create_file_sh(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path)

        content = r'''#!/bin/bash

source .venv/bin/activate

mkdir -p logs

trap 'kill 0' SIGINT SIGTERM EXIT

celery -A celery_app worker -l info > logs/celery_worker.log 2>&1 &
celery -A celery_app beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler > logs/celery_beat.log 2>&1 &

wait
'''
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="start_celery.sh",
            content=content
        )

