from gen.helpers.helper_file import HelperFile


class DjGenerateTodoMD:

    def invoke(self, full_path, project_name):
        """
        Genera el archivo.
        """

        content = f'''# {project_name}
        
```sh

```

## TODOS Pendientes:
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=full_path,
            file_name="X.php",
            content=content
        )

