import os
from gen.python_django.helpers.helper_file import helper_append_content, helper_create_init_file
from helpers.helper_print import print_message, GREEN, CYAN



def generate_logs(full_path, project_name_format, app_main, venv_python):
    create_file(full_path, project_name_format, app_main, venv_python)
    update_settings(full_path, project_name_format, app_main)
    create_folder_logs(full_path, project_name_format, app_main)


def create_file(full_path, project_name_format, app_main, venv_python):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "core", "logs")
    file_path = os.path.join(folder_path, "logging_handlers.py")

    os.makedirs(folder_path, exist_ok=True)
    
    # create init file
    helper_create_init_file(folder_path)
    

    content = r'''import os
import logging
from datetime import datetime


class DailyFileHandler(logging.FileHandler):
    def __init__(self, log_dir, prefix, encoding=None, delay=False):
        self.log_dir = log_dir
        self.prefix = prefix
        self.current_date = datetime.now().strftime("%Y_%m_%d")

        os.makedirs(self.log_dir, exist_ok=True)

        filename = self._build_filename()
        super().__init__(filename, mode="a", encoding=encoding, delay=delay)

    def _build_filename(self):
        return os.path.join(
            self.log_dir,
            f"{self.prefix}_{self.current_date}.log"
        )

    def emit(self, record):
        new_date = datetime.now().strftime("%Y_%m_%d")

        if new_date != self.current_date:
            self.current_date = new_date

            if self.stream:
                self.stream.close()
                self.stream = None

            self.baseFilename = os.path.abspath(self._build_filename())
            self.stream = self._open()

        super().emit(record)
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
        
        
def update_settings(full_path, project_name_format, app_main):
    str = r"""
## Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "file": {
            "level": "ERROR",
            "class": "core.logs.logging_handlers.DailyFileHandler",
            "log_dir": os.path.join(BASE_DIR, "logs"),
            "prefix": "django_log",
            "formatter": "verbose",
            "encoding": "utf-8",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}

"""
    
    helper_append_content(
        full_path, 
        f"{app_main}/settings.py", 
        str
    )
    
    
    
def create_folder_logs(full_path, project_name_format, app_main):
    logs_folder_path = os.path.join(full_path, "logs")
    os.makedirs(logs_folder_path, exist_ok=True)
    