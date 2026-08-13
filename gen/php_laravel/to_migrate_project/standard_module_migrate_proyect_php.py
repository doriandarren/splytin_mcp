import os
import shutil
from gen.helpers.helper_menu import pause


def standard_module_migrate_proyect_php(
    full_path_origin: str, 
    full_path_destination: str
) -> None:
    
    enums_path_origin = os.path.join(full_path_origin, "app", "Enums")
    enums_path_destination = os.path.join(full_path_destination, "app", "Enums")
    migrate_enums(enums_path_origin, enums_path_destination)
    
    
    
    
    
def migrate_enums(
    enums_path_origin: str, 
    enums_path_destination: str
) -> None:
    
    # Migrar la carpeta app/Enums de fullt_path_origin a fullt_path_destination

    if not os.path.isdir(enums_path_origin):
        print(f"\n❌ No existe la carpeta origen:")
        print(enums_path_origin)
        pause()
        return
    
    try:
        
        shutil.copytree(
            enums_path_origin,
            enums_path_destination,
            dirs_exist_ok=True
        )

        print("\n✅ Carpeta app/Enums migrada correctamente")
        print(f"📂 Origen: {enums_path_origin}")
        
    except PermissionError:
        print("\n❌ No tienes permisos para copiar la carpeta.")

    except OSError as error:
        print(f"\n❌ Error al migrar app/Enums: {error}")
    