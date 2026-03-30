from __future__ import annotations

from typing import Any

from gen.helpers.helper_columns import parse_columns_input


DEFAULT_DJANGO_COMPONENTS = [
    "api_route",
    "api_serializer",
    "api_wiewset",
    "api_model",
    "api_service",
]


def _full_path(base_path: str, project_name: str) -> str:
    return f"{base_path.rstrip('/')}/{project_name}"


def _normalize_columns(columns: str | list[dict[str, Any]]) -> list[dict[str, Any]]:
    if isinstance(columns, str):
        return parse_columns_input(columns)
    return columns


def create_python_django_project_service(
    project_name: str,
    project_path: str,
    app_main: str = "main",
) -> dict[str, Any]:
    from gen.helpers.helper_string import normalize_project_name
    from gen.python_django.helpers.helper_virtual_env import get_venv_python
    from gen.python_django.to_create_project.core.generate_core_file_init import (
        generate_code_file_init,
    )
    from gen.python_django.to_create_project.core.generate_core_models import (
        generate_core_models,
    )
    from gen.python_django.to_create_project.core.generate_file_helpers import (
        generate_file_helpers,
    )
    from gen.python_django.to_create_project.core.generate_http import generate_http
    from gen.python_django.to_create_project.core.generate_message_channel import (
        generate_message_channel,
    )
    from gen.python_django.to_create_project.generate_api_doc import generate_api_doc
    from gen.python_django.to_create_project.generate_by_command_line import (
        generate_by_command_line as generate_python_django_by_command_line,
    )
    from gen.python_django.to_create_project.generate_cors import generate_cors
    from gen.python_django.to_create_project.generate_cron import generate_cron
    from gen.python_django.to_create_project.generate_django import generate_django
    from gen.python_django.to_create_project.generate_env import generate_env
    from gen.python_django.to_create_project.generate_gitignore import generate_gitignore
    from gen.python_django.to_create_project.generate_page_home import generate_page_home
    from gen.python_django.to_create_project.generate_passenger_wsgi import (
        generate_passenger_wsgi,
    )
    from gen.python_django.to_create_project.generate_postgres import generate_postgres
    from gen.python_django.to_create_project.generate_readme import generate_readme
    from gen.python_django.to_create_project.generate_simplejwt import (
        generate_simplejwt,
    )
    from gen.python_django.to_create_project.generate_static_files import (
        generate_static_files,
    )
    from gen.python_django.to_create_project.generate_todo_md import generate_todo_md
    from gen.python_django.to_create_project.modules.generate_module_devs import (
        generate_module_devs,
    )
    from gen.python_django.to_create_project.modules.generate_module_users import (
        generate_module_users,
    )

    full_path = _full_path(project_path, project_name)
    project_name_format = normalize_project_name(project_name)

    generate_python_django_by_command_line(full_path, project_name_format, app_main)
    generate_gitignore(full_path)
    generate_passenger_wsgi(full_path, app_main)
    generate_readme(full_path, project_name)
    generate_todo_md(full_path, project_name)

    venv_python = get_venv_python(full_path)

    generate_django(full_path, project_name_format, app_main, venv_python)
    generate_env(full_path, project_name_format, app_main, venv_python)
    generate_static_files(full_path, app_main)
    generate_postgres(full_path, project_name_format, app_main, venv_python)
    generate_api_doc(full_path, project_name_format, app_main, venv_python)
    generate_simplejwt(full_path, project_name_format, app_main, venv_python)
    generate_code_file_init(full_path)
    generate_cors(full_path, project_name_format, app_main, venv_python)
    generate_file_helpers(full_path)
    generate_http(full_path)
    generate_message_channel(full_path)
    generate_core_models(full_path)
    generate_page_home(full_path, project_name_format, app_main)
    generate_module_users(full_path, project_name_format, app_main)
    generate_module_devs(full_path, project_name_format, app_main)
    generate_cron(full_path, project_name_format, app_main, venv_python)
    

    return {
        "generator": "python_django_project",
        "project_name": project_name,
        "project_name_format": project_name_format,
        "app_name": app_main,
        "full_path": full_path,
    }


def create_python_django_crud_service(
    full_path: str,
    app_main: str,
    singular_name: str,
    plural_name: str,
    columns: str | list[dict[str, Any]],
    components: list[str] | None = None,
) -> dict[str, Any]:
    from gen.python_django.to_create_module_crud.standard_module_crud_python_django import (
        standard_module_crud_python_django,
    )

    normalized_columns = _normalize_columns(columns)
    selected_components = components or DEFAULT_DJANGO_COMPONENTS

    standard_module_crud_python_django(
        full_path,
        app_main,
        singular_name,
        plural_name,
        normalized_columns,
        selected_components,
    )

    return {
        "generator": "python_django_crud",
        "full_path": full_path,
        "app_main": app_main,
        "singular_name": singular_name,
        "plural_name": plural_name,
        "components": selected_components,
        "columns": normalized_columns,
    }


def create_react_project_service(
    project_name: str,
    project_path: str,
) -> dict[str, Any]:
    from gen.react.to_create_project.file_helpers.generate_helpers import (
        generate_helpers,
    )
    from gen.react.to_create_project.generate_by_command_line import (
        generate_by_command_line as generate_react_by_command_line,
    )
    from gen.react.to_create_project.generate_env import (
        generate_env as generate_react_env,
    )
    from gen.react.to_create_project.generate_folder_api import generate_folder_api
    from gen.react.to_create_project.generate_gitignore import (
        generate_gitignore as generate_react_gitignore,
    )
    from gen.react.to_create_project.generate_images import generate_images
    from gen.react.to_create_project.generate_index_html import generate_index_html
    from gen.react.to_create_project.generate_module_auth import generate_module_auth
    from gen.react.to_create_project.generate_module_dashboard import (
        generate_module_dashboard,
    )
    from gen.react.to_create_project.generate_module_profile import (
        generate_module_profile,
    )
    from gen.react.to_create_project.generate_module_public import generate_module_public
    from gen.react.to_create_project.generate_modules import generate_modules
    from gen.react.to_create_project.generate_private_layouts import (
        generate_private_layouts,
    )
    from gen.react.to_create_project.generate_public_layouts import (
        generate_public_layouts,
    )
    from gen.react.to_create_project.generate_react_router import (
        generate_react_router,
    )
    from gen.react.to_create_project.generate_readme import (
        generate_readme as generate_react_readme,
    )
    from gen.react.to_create_project.generate_redux import generate_redux
    from gen.react.to_create_project.generate_styles import generate_styles
    from gen.react.to_create_project.generate_translate import generate_translate
    from gen.react.to_create_project.components.generate_components import (
        generate_components,
    )
    from gen.react.to_create_project.role_permissions.generate_helper_allowed_paths import (
        generate_helper_allowed_paths,
    )
    from gen.react.to_create_project.role_permissions.generate_helper_build_accessible_nav import (
        generate_generate_helper_build_accessible_nav,
    )
    from gen.react.to_create_project.role_permissions.generate_helper_role_menu_access import (
        generate_helper_role_menu_access,
    )

    full_path = _full_path(project_path, project_name)

    generate_react_by_command_line(full_path)
    generate_styles(full_path)
    generate_images(full_path)
    generate_private_layouts(full_path)
    generate_public_layouts(full_path)
    generate_module_public(full_path)
    generate_react_router(full_path)
    generate_components(full_path)
    generate_module_dashboard(full_path)
    generate_module_auth(full_path, project_name)
    generate_module_profile(full_path)
    generate_modules(full_path)
    generate_redux(full_path)
    generate_helpers(full_path)
    generate_translate(full_path)
    generate_react_env(full_path)
    generate_react_gitignore(full_path)
    generate_react_readme(full_path)
    generate_index_html(full_path)
    generate_folder_api(full_path)
    generate_helper_allowed_paths(full_path)
    generate_generate_helper_build_accessible_nav(full_path)
    generate_helper_role_menu_access(full_path)

    return {
        "generator": "react_project",
        "project_name": project_name,
        "full_path": full_path,
    }


def create_php_project_service(
    project_name: str,
    project_path: str,
) -> dict[str, Any]:
    from gen.php.to_create_project.auth.generate_module_auth import (
        generate_module_auth as generate_php_module_auth,
    )
    from gen.php.to_create_project.batch_processes.generate_batch_processes import (
        generate_batch_processes,
    )
    from gen.php.to_create_project.dashboards.generate_dashboard import (
        generate_dashboard,
    )
    from gen.php.to_create_project.dev.generate_execute_controller import (
        generate_execute_controller,
    )
    from gen.php.to_create_project.dev.generate_route_test import generate_route_test
    from gen.php.to_create_project.dev.generate_test_controller import (
        generate_test_controller,
    )
    from gen.php.to_create_project.excel.generate_maatwebsite_excel import (
        generate_maatwebsite_excel,
    )
    from gen.php.to_create_project.fpdf_merge.generate_fpdf_merge import (
        generate_fpdf_merge,
    )
    from gen.php.to_create_project.generate_base_controller import (
        generate_base_controller,
    )
    from gen.php.to_create_project.generate_by_command_line import (
        generate_by_command_line as generate_php_by_command_line,
    )
    from gen.php.to_create_project.generate_enums import generate_enums
    from gen.php.to_create_project.images.generate_company_logos import (
        generate_company_logos,
    )
    from gen.php.to_create_project.scripts.generate_shared_postman_collections import (
        generate_shared_postman_collections,
    )
    from gen.php.to_create_project.shared.generate_shared import generate_shared
    from gen.php.to_create_project.snappy.generate_snappy import generate_snappy
    from gen.php.to_create_project.updates.update_app_php import update_app_php
    from gen.php.to_create_project.updates.update_bootstrap_app_php import (
        update_bootstrap_app_php,
    )
    from gen.php.to_create_project.updates.update_gitignore import update_gitignore
    from gen.php.to_create_project.updates.update_model_user_php import (
        update_model_user,
    )
    from gen.php.to_create_project.updates.update_readme import update_readme
    from gen.php.to_create_project.updates.update_route_api_php import (
        update_route_api_php,
    )
    from gen.php.to_create_project.updates.update_welcome_blade import (
        update_welcome_blade,
    )
    from gen.php.to_create_project.utilities.generate_utilities import (
        generate_utilities,
    )

    full_path = _full_path(project_path, project_name)

    generate_php_by_command_line(full_path)
    generate_snappy(full_path)
    generate_fpdf_merge(full_path)
    generate_maatwebsite_excel(full_path)
    generate_enums(full_path)
    generate_batch_processes(full_path)
    generate_base_controller(full_path)
    generate_php_module_auth(full_path)
    generate_shared(full_path)
    generate_dashboard(full_path)
    generate_utilities(full_path)
    update_model_user(full_path)
    update_app_php(full_path)
    update_bootstrap_app_php(full_path)
    update_readme(full_path)
    update_gitignore(full_path)
    generate_execute_controller(full_path)
    generate_test_controller(full_path)
    generate_route_test(full_path)
    generate_company_logos(full_path)
    update_welcome_blade(full_path)
    generate_shared_postman_collections(full_path, project_name)
    update_route_api_php(full_path)

    return {
        "generator": "php_project",
        "project_name": project_name,
        "full_path": full_path,
    }
