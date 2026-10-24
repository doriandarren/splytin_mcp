import os
from helpers.helper_menu import pause
from helpers.helper_print import camel_to_first_letter_lower, camel_to_kebab, camel_to_snake
from helpers.helper_string import normalize_project_name



class StandardModuleCrudReactTs:

    def invoke(
        self,
        full_path,
        namespace,
        version_api,
        folder_group,
        singular_name,
        plural_name,
        columns,
        input_menu_checkbox=None
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
        #     generate_route(
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
        #     generate_list_page(
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
        #     generate_create_page(
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
        #     generate_edit_page(
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
        #     generate_service_file(
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