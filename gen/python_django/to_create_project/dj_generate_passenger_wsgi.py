import os
from gen.helpers.helper_file import HelperFile


class DjGeneratePassengerWSGI:

    def invoke(self, full_path, app_main):
        self.create_passenger_wsgi(full_path, app_main)
        self.create_folder_tmp(full_path, app_main)

    def create_passenger_wsgi(self, full_path, app_main):
        """
        Genera passenger_wsgi.py
        """

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

        content = content.replace("__APP_MAIN__", app_main)

        HelperFile.write(
            folder_path=full_path,
            file_name="passenger_wsgi.py",
            content=content
        )




    def create_folder_tmp(self, full_path, app_main):
        """
        Genera tmp/restart.txt
        """

        folder_path = os.path.join(full_path, "tmp")

        HelperFile.write(
            folder_path=folder_path,
            file_name="restart.txt",
            content=""
        )