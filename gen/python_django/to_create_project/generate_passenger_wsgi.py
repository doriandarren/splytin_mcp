import os
from gen.helpers.helper_print import print_message, GREEN, CYAN

def generate_passenger_wsgi(full_path, app_main):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path)
    file_path = os.path.join(folder_path, "passenger_wsgi.py")

    os.makedirs(folder_path, exist_ok=True)

    content = r'''import os
import sys
import traceback
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
LOG_FILE = PROJECT_DIR / "passenger_debug.log"

with open(LOG_FILE, "a") as f:
    f.write("START\n")
    f.write(f"PROJECT_DIR={PROJECT_DIR}\n")
    f.write(f"sys.executable={sys.executable}\n")
    f.write(f"sys.path(before)={sys.path}\n")

try:
    sys.path.insert(0, str(PROJECT_DIR))

    with open(LOG_FILE, "a") as f:
        f.write(f"sys.path(after)={sys.path}\n")

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

    with open(LOG_FILE, "a") as f:
        f.write(f"DJANGO_SETTINGS_MODULE={os.environ.get('DJANGO_SETTINGS_MODULE')}\n")

    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()

    with open(LOG_FILE, "a") as f:
        f.write("WSGI LOADED OK\n")

except Exception:
    with open(LOG_FILE, "a") as f:
        f.write("ERROR START\n")
        f.write(traceback.format_exc())
        f.write("\nERROR END\n")
    raise
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)