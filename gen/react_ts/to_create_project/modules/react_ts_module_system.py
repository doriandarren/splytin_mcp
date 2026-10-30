import os
from gen.helpers.helper_file import HelperFile


class ReactTsModuleSystem:
    
    def invoke(self, full_path):
        self.create_system_tsx(full_path)
        
        

    def create_system_tsx(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "src", "modules", "private", "systems", "pages")

        content = r'''// src/modules/private/systems/pages/SystemPage.tsx
export const SystemPage = () => {
  return (
    <div>SystemPage</div>
  )
}
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="SystemPage.tsx",
            content=content
        )