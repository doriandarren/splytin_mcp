import os
import json

from helpers.helper_file import HelperFile
from gen.php_laravel.to_create_project.helpers.postman.helper_laravel_postman import HelperLaravelPostman
from helpers.helper_print import dd


class LaravelPostman:

    def invoke(self, full_path, project_name, domain_name, password):
        """
        Genera la colección Postman del proyecto Laravel.
        """

        folder_path = os.path.join(full_path, "public", "SCRIPTS")
        

        collection = HelperLaravelPostman.build_collection(
            project_name=project_name,
            domain_name=domain_name,
            password=password
        )
        

        content = json.dumps(
            collection,
            ensure_ascii=False,
            indent=2
        )

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name=f"API-{project_name}.postman.collection.json",
            content=content
        )
        
        
        


