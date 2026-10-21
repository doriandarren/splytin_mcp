import os
from gen.helpers.helper_print import print_message, GREEN, CYAN, run_command_debug
from gen.python_django.helpers.helper_file import helper_create_init_file


class DjGenerateApp:

    def invoke(self, full_path, plural_name_snake, venv_python, manage_py_path=None):
        self.install_app(full_path, plural_name_snake, venv_python)


    def install_app(self, full_path, plural_name_snake, venv_python):
        apps_path = os.path.join(full_path, "apps")
        os.makedirs(apps_path, exist_ok=True)

        helper_create_init_file(apps_path)

        app_path = os.path.join(apps_path, plural_name_snake)

        if os.path.exists(app_path):
            print_message(f"App {plural_name_snake} ya instalada.", GREEN)
            return

        command = f'"{venv_python}" -m django startapp {plural_name_snake} "{app_path}"'
        run_command_debug(command, cwd=full_path)

        helper_create_init_file(app_path)

        apps_py_path = os.path.join(app_path, "apps.py")
        if os.path.exists(apps_py_path):
            with open(apps_py_path, "r", encoding="utf-8") as file:
                content = file.read()

            content = content.replace(
                f"name = '{plural_name_snake}'",
                f"name = 'apps.{plural_name_snake}'"
            )

            with open(apps_py_path, "w", encoding="utf-8") as file:
                file.write(content)

        print_message(f"App {plural_name_snake} instalada correctamente.", GREEN)