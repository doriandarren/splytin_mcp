import os
from gen.helpers.helper_file import HelperFile


class DjGenerateCoreFileInit:

    def invoke(self, full_path):
        """
        Genera el archivo __init__.py en core.
        """

        folder_path = os.path.join(full_path, "core")

        content = ""

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="__init__.py",
            content=content
        )
        
        

