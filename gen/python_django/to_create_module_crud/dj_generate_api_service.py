
import os
from gen.helpers.helper_file import HelperFile



class DjGenerateApiService:

    def invoke(
        self,
        full_path,
        project_name,
        singular_name,
        plural_name,
        singular_name_kebab,
        plural_name_kebab,
        singular_name_snake,
        plural_name_snake,
        singular_first_camel,
        plural_first_camel,
        columns,
    ):
        self.create_init_file(full_path, plural_name_snake)

        self.create_file(
            full_path,
            project_name,
            singular_name,
            plural_name,
            singular_name_kebab,
            plural_name_kebab,
            singular_name_snake,
            plural_name_snake,
            singular_first_camel,
            plural_first_camel,
            columns,
        )

    def create_init_file(self, full_path, plural_name_snake):
        """
        Genera __init__.py dentro de services.
        """

        folder_path = os.path.join(
            full_path, "apps", plural_name_snake, "services"
        )

        HelperFile.write(
            folder_path=folder_path,
            file_name="__init__.py",
            content=""
        )
        
        
        

    def create_file(
        self,
        full_path,
        project_name,
        singular_name,
        plural_name,
        singular_name_kebab,
        plural_name_kebab,
        singular_name_snake,
        plural_name_snake,
        singular_first_camel,
        plural_first_camel,
        columns,
    ):
        """
        Genera el archivo del servicio CRUD.
        """

        folder_path = os.path.join(
            full_path, "apps", plural_name_snake, "services"
        )

        content = f'''from apps.{plural_name_snake}.models import {singular_name}


class {singular_name}Service:

    def list(self):
        return {singular_name}.objects.all()

    def show(self, id):
        return {singular_name}.objects.filter(id=id).first()

    def store(self, model: {singular_name}):
        model.save()
        return model

    def update(self, id, data: dict):
        model = self.show(id)

        if not model:
            return None
'''

        # Generar las asignaciones de update()
        for column in columns:
            column_name = column["name"]

            content += f'''
        if "{column_name}" in data:
            model.{column_name} = data["{column_name}"]
'''

        content += '''
        model.save()
        return model

    def destroy(self, id) -> bool:
        model = self.show(id)

        if not model:
            return False

        model.delete()
        return True
'''

        # Generar el método set_<modelo>()
        content += f'''

    def set_{singular_name_snake}(
        self,'''

        for column in columns:
            column_name = column["name"]

            content += f'''
        {column_name},'''

        content += f'''
    ) -> {singular_name}:
        model = {singular_name}()
'''

        # Generar las asignaciones del nuevo modelo
        for column in columns:
            column_name = column["name"]

            content += f'        model.{column_name} = {column_name}\n'

        content += '''
        return model
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name=f"{singular_name_snake}_service.py",
            content=content
        )
