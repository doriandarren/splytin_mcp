import os
import json
from helpers.helper_print import dd, print_green, print_red


class ReactTsCrudTranslate:

    def invoke(
        self,
        full_path,
        namespace,
        version_api,
        folder_group,
        project_name,
        singular_name,
        plural_name,
        singular_name_camel,
        plural_name_camel,
        singular_name_kebab,
        plural_name_kebab,
        singular_name_snake,
        plural_name_snake,
        columns
    ):
        """
        Genera el archivo.
        """

        self.update_en(
            full_path,
            namespace,
            version_api,
            folder_group,
            project_name,
            singular_name,
            plural_name,
            singular_name_camel,
            plural_name_camel,
            singular_name_kebab,
            plural_name_kebab,
            singular_name_snake,
            plural_name_snake,
            columns
        )
        

        self.update_es(
            full_path,
            namespace,
            version_api,
            folder_group,
            project_name,
            singular_name,
            plural_name,
            singular_name_camel,
            plural_name_camel,
            singular_name_kebab,
            plural_name_kebab,
            singular_name_snake,
            plural_name_snake,
            columns
        )
        



    def update_en(
        self,
        full_path,
        namespace,
        version_api,
        folder_group,
        project_name,
        singular_name,
        plural_name,
        singular_name_camel,
        plural_name_camel,
        singular_name_kebab,
        plural_name_kebab,
        singular_name_snake,
        plural_name_snake,
        columns
    ):
        """
        Agrega las traducciones del módulo al common.json en inglés.
        """

        main_path = os.path.join(
            full_path, "src", "i18n", "locales", "en", "common.json"
        )

        # Leer JSON existente
        with open(main_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Nombre del módulo
        module_key = f"{plural_name_snake}_module"

        # Agregar traducciones
        data[module_key] = {
            "fields": {
                column["name"]: column["name"].replace("_", " ").capitalize()
                for column in columns
            }
        }

        # Guardar JSON actualizado
        with open(main_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            file.write("\n")

        print_green(f"Translations updated: {module_key}")
        

    def update_es(
        self,
        full_path,
        namespace,
        version_api,
        folder_group,
        project_name,
        singular_name,
        plural_name,
        singular_name_camel,
        plural_name_camel,
        singular_name_kebab,
        plural_name_kebab,
        singular_name_snake,
        plural_name_snake,
        columns
    ):
        """
        Agrega las traducciones del módulo al common.json en inglés.
        """

        main_path = os.path.join(
            full_path, "src", "i18n", "locales", "es", "common.json"
        )

        # Leer JSON existente
        with open(main_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Nombre del módulo
        module_key = f"{plural_name_snake}_module"

        # Agregar traducciones
        data[module_key] = {
            "fields": {
                column["name"]: column["name"].replace("_", " ").capitalize()
                for column in columns
            }
        }

        # Guardar JSON actualizado
        with open(main_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            file.write("\n")

        print_green(f"Translations updated: {module_key}")