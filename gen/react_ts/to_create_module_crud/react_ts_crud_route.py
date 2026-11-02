
from gen.helpers.helper_print import print_green
from gen.react_ts.helpers.helper_react_ts_router import HelperReactTsRouter




class ReactTsCrudRoute:

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
        Actualiza las rutas del CRUD.
        """
        
        if not HelperReactTsRouter.validate(full_path):
            return False

        # Imports
        if not HelperReactTsRouter.add_import(
            full_path,
            namespace,
            plural_name_snake,
            f"{singular_name}Page"
        ):
            return False

        if not HelperReactTsRouter.add_import(
            full_path,
            namespace,
            plural_name_snake,
            f"{singular_name}CreatePage"
        ):
            return False

        if not HelperReactTsRouter.add_import(
            full_path,
            namespace,
            plural_name_snake,
            f"{singular_name}UpdatePage"
        ):
            return False

        # Ruta listado
        if not HelperReactTsRouter.add_route(
            full_path,
            plural_name_kebab,
            f"{singular_name}Page"
        ):
            return False

        # Ruta Create
        if not HelperReactTsRouter.add_route(
            full_path,
            f"{plural_name_kebab}/create",
            f"{singular_name}CreatePage"
        ):
            return False

        # Ruta Update
        if not HelperReactTsRouter.add_route(
            full_path,
            f"{plural_name_kebab}/:id/edit",
            f"{singular_name}UpdatePage"
        ):
            return False

        print_green(
            f"CRUD '{singular_name}' registrado correctamente."
        )
        
        return True
