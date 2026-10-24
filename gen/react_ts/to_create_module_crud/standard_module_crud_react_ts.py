import os
from gen.helpers.helper_menu import pause
from gen.helpers.helper_print import camel_to_first_letter_lower, camel_to_kebab, camel_to_snake
from gen.helpers.helper_string import normalize_project_name



class StandardModuleCrudReactTs:

    def invoke(
        self,
        full_path,
        namespace,
        singular_name,
        plural_name,
        columns,
        input_menu_checkbox=None,
        version_api=None,
        folder_group=None
    ):

        # Input Default
        if input_menu_checkbox is None:
            input_menu_checkbox = ["route", "list", "create", "edit", "service"]

        # Convertir nombres
        singular_name_kebab = camel_to_kebab(singular_name)
        plural_name_kebab = camel_to_kebab(plural_name)
        singular_name_snake = camel_to_snake(singular_name)
        plural_name_snake = camel_to_snake(plural_name)
        singular_name_camel = camel_to_first_letter_lower(singular_name)
        plural_name_camel = camel_to_first_letter_lower(plural_name)
        ## Project Name
        temp_name = os.path.basename(full_path.rstrip(os.sep))
        project_name = normalize_project_name(temp_name)


        # TODO refactor
        # if "route" in input_menu_checkbox:
        #     obj = XGenerateRoute()
        #     obj.invoke(
        #         full_path,
        #         namespace,
        #         version_api,
        #         folder_group,
        #         project_name,
        #         singular_name,
        #         plural_name,
        #         singular_name_camel,
        #         plural_name_camel,
        #         singular_name_kebab,
        #         plural_name_kebab,
        #         singular_name_snake,
        #         plural_name_snake,
        #         columns
        #     )


        # if "list" in input_menu_checkbox:
        #     obj = XGenerateListPage()
        #     obj.invoke(
        #         full_path,
        #         namespace,
        #         version_api,
        #         folder_group,
        #         project_name,
        #         singular_name,
        #         plural_name,
        #         singular_name_camel,
        #         plural_name_camel,
        #         singular_name_kebab,
        #         plural_name_kebab,
        #         singular_name_snake,
        #         plural_name_snake,
        #         columns
        #     )

        # if "create" in input_menu_checkbox:
        #     obj = XGenerateCreatePage()
        #     obj.invoke(
        #         full_path,
        #         namespace,
        #         version_api,
        #         folder_group,
        #         project_name,
        #         singular_name,
        #         plural_name,
        #         singular_name_camel,
        #         plural_name_camel,
        #         singular_name_kebab,
        #         plural_name_kebab,
        #         singular_name_snake,
        #         plural_name_snake,
        #         columns
        #     )

        # if "edit" in input_menu_checkbox:
        #     obj = XGenerateEditPage()
        #     obj.invoke(
        #         full_path,
        #         namespace,
        #         version_api,
        #         folder_group,
        #         project_name,
        #         singular_name,
        #         plural_name,
        #         singular_name_camel,
        #         plural_name_camel,
        #         singular_name_kebab,
        #         plural_name_kebab,
        #         singular_name_snake,
        #         plural_name_snake,
        #         columns
        #     )

        # if "service" in input_menu_checkbox:
        #     obj = XGenerateServiceFile()
        #     obj.invoke(
        #         full_path,
        #         namespace,
        #         version_api,
        #         folder_group,
        #         project_name,
        #         singular_name,
        #         plural_name,
        #         singular_name_camel,
        #         plural_name_camel,
        #         singular_name_kebab,
        #         plural_name_kebab,
        #         singular_name_snake,
        #         plural_name_snake,
        #         columns
        #     )
        pause()   