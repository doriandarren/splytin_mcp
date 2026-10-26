import os
from gen.helpers.helper_file import HelperFile



class ReactTsGoogleFonts:
    def invoke(self, full_path, project_name):
        self.update_index_html(full_path, project_name)
        self.update_index_css(full_path)
      

    def update_index_html(self, full_path, project_name):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path)

        content = r'''<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>__PROJECT_NAME__</title>
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat+Alternates:wght@300;400;700&display=swap" rel="stylesheet">

  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
'''

        content = content.replace("__PROJECT_NAME__", project_name)


        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="index.html",
            content=content
        )
        
        
    
    def update_index_css(self, full_path):
      
      content = """<@theme {
  --font-montserrat: "Montserrat Alternates", sans-serif;
}"""
      
      
      HelperFile.append(
        full_path,
        "index.css",
        content
      )