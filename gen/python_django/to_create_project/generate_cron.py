import os
from gen.helpers.helper_print import print_message, GREEN, CYAN, run_command
from gen.python_django.helpers.helper_file import helper_append_content, helper_update_list

def generate_cron(full_path, project_name_format, app_name, venv_python):
    """
    Genera el archivo
    """    
    install_cron(full_path, venv_python)
    update_settings(full_path, project_name_format, app_name)
    create_file_init(full_path)
    create_file_celery(full_path, project_name_format, app_name)
    create_file_cron_devs(full_path)



def install_cron(full_path, venv_python):
    print_message("Instalando Celery...", CYAN)
    run_command(f'"{venv_python}" -m pip install celery django-celery-beat redis', cwd=full_path)
    print_message("Celery instalado correctamente.", GREEN)
    

    
def update_settings(full_path, project_name_format, app_name):
    
    helper_update_list(
        full_path, 
        f"{app_name}/settings.py", 
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
        f"{app_name}/settings.py", 
        str
    )
    
   

def create_file_init(full_path):
    """
    Genera el archivo init
    """
    
    # File __init__.py
    folder_path = os.path.join(full_path, "celery_app")
    file_path = os.path.join(folder_path, "__init__.py")

    os.makedirs(folder_path, exist_ok=True)

    content = f'''from .celery import app

__all__ = ("app",)
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)   
   
   
   
    
def create_file_celery(full_path, project_name_format, app_name):
    """
    Genera el archivo init
    """
    
    # File celery.py
    folder_path = os.path.join(full_path, "celery_app")
    file_path = os.path.join(folder_path, "celery.py")

    os.makedirs(folder_path, exist_ok=True)

    content = f'''import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{app_name}.settings")

app = Celery("{app_name}")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)   



def create_file_cron_devs(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "apps", "devs")
    file_path = os.path.join(folder_path, "tasks.py")

    os.makedirs(folder_path, exist_ok=True)

    content = r'''from celery import shared_task
from django.utils import timezone


@shared_task
def start():
    now = timezone.now()
    print(f"Hola desde Celery: {now}")
    return f"Ejecutado en {now}"
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)

