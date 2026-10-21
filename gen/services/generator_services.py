from __future__ import annotations

from typing import Any

import os
from dotenv import load_dotenv
from gen.helpers.helper_columns import parse_columns_input
from gen.helpers.helpers import dd
from gen.php_laravel.to_create_project.generate_api_controller import generate_api_controller
from gen.php_laravel.to_create_project.generate_default_role_permissions import generate_default_role_permissions
from gen.php_laravel.to_create_project.generate_query_filter import generate_query_filter
from gen.php_laravel.to_create_project.generate_test_email import generate_test_mail
from gen.php_laravel.to_create_project.requests.generate_base_api_request import generate_base_api_request
from gen.php_laravel.to_create_project.traits.generate_trait_api_response import generate_trait_api_response
from gen.php_laravel.to_create_project.traits.generate_trait_tracks_users import generate_trait_tracks_users
from gen.php_laravel.to_create_project.updates.update_ability_user_model import update_ability_user_model
from gen.php_laravel.to_create_project.updates.update_app_service_provider import update_app_service_provider
from gen.php_laravel.to_create_project.updates.update_role_user_model import update_role_user_model
from gen.python_django.helpers import helper_domain
from gen.python_django.to_create_project.core.dj_generate_api_response import DjGenerateApiResponse
from gen.python_django.to_create_project.core.dj_generate_core_models import DjGenerateCoreModels
from gen.python_django.to_create_project.core.dj_generate_message_channel import DjGenerateMessageChannel
from gen.python_django.to_create_project.core.dj_generate_http import DjGenerateHttp
from gen.python_django.to_create_project.core.dj_generate_file_helpers import DjGenerateFileHelpers
from gen.python_django.to_create_project.core.dj_generate_core_file_init import DjGenerateCoreFileInit
from gen.python_django.to_create_project.core.dj_generate_custom_logging import DjGenerateCustomLogging
from gen.python_django.to_create_project.dj_generate_cors import DjGenerateCors
from gen.python_django.to_create_project.dj_generate_cron import DjGenerateCron
from gen.python_django.to_create_project.modules.dj_generate_module_auth import DjGenerateModuleAuth
from gen.python_django.to_create_project.modules.dj_generate_module_devs import DjGenerateModuleDevs
from gen.python_django.to_create_project.modules.dj_generate_module_users import DjGenerateModuleUsers
from gen.python_django.to_create_project.dj_generate_page_home import DjGeneratePageHome
from gen.python_django.to_create_project.dj_generate_api_doc import DjGenerateApiDoc
from gen.python_django.to_create_project.dj_generate_djangorestframework_jsonapi import DjGenerateDjangorestframeworkJsonapi
from gen.python_django.to_create_project.dj_generate_postgres import DjGeneratePostgre
from gen.python_django.to_create_project.dj_generate_django import DjGenerateDjango
from gen.python_django.to_create_project.dj_generate_env import DjGenerateEnv
from gen.python_django.to_create_project.dj_generate_gitignore import DjGenerateIgnore
from gen.python_django.to_create_project.dj_generate_postman import DjGeneratePostman
from gen.python_django.to_create_project.dj_generate_requirements_txt import DjGenerateRequirementsTxt
from gen.python_django.to_create_project.dj_generate_command_line import DjGenerateCommandLine
from gen.python_django.to_create_project.dj_generate_passenger_wsgi import DjGeneratePassengerWSGI
from gen.python_django.to_create_project.dj_generate_readme import DjGenerateReadme
from gen.python_django.to_create_project.dj_generate_todo_md import DjGenerateTodoMD
from gen.python_django.to_create_project.dj_generate_static_files import DjGenerateStaticFiles
from gen.python_django.to_create_project.statics.dj_generate_media import DjGenerateMedia


load_dotenv()


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



    full_path = _full_path(project_path, project_name)
    project_name_format = normalize_project_name(project_name)
    
    domain_name = helper_domain.helper_domain_name(project_name)
    
    
    # CommandLine & return venv_python
    obj = DjGenerateCommandLine()
    venv_python = obj.invoke(full_path, project_name_format, app_main)
    
    
    # Gitignore
    gitignore = DjGenerateIgnore()
    gitignore.invoke(full_path)
    
    
    # PassengerWSGI
    obj = DjGeneratePassengerWSGI()
    obj.invoke(full_path, app_main)
    
    
    # Readme
    obj = DjGenerateReadme()
    obj.invoke(full_path, project_name, project_name_format, domain_name)
    
    # FileTODO
    obj = DjGenerateTodoMD()
    obj.invoke(full_path, project_name)
    
    
    # Django
    obj = DjGenerateDjango()
    obj.invoke(full_path, project_name_format, app_main, venv_python)
    
    
    # Env
    obj = DjGenerateEnv()
    obj.invoke(full_path, project_name_format, app_main, venv_python)
    
    
    # Media
    obj = DjGenerateMedia()
    obj.invoke(full_path, project_name_format, app_main, venv_python)
    
    
    #Static Files
    obj = DjGenerateStaticFiles()
    obj.invoke(full_path, app_main)
    
    
    # Postgre
    obj = DjGeneratePostgre()
    obj.invoke(full_path, project_name_format, app_main, venv_python)
    
    
    # APIDoc
    obj = DjGenerateApiDoc()
    obj.invoke(full_path, project_name_format, app_main, venv_python)
    
    
    # CoreFileInit
    obj = DjGenerateCoreFileInit()
    obj.invoke(full_path)
    
    
    # Cors
    obj = DjGenerateCors()
    obj.invoke(full_path, project_name_format, app_main, venv_python)
    
    
    # File Helpers
    obj = DjGenerateFileHelpers()
    obj.invoke(full_path)
    
    
    # Core - Http
    obj = DjGenerateHttp()
    obj.invoke(full_path)
    
    
    # Core - Message Channel
    obj = DjGenerateMessageChannel()
    obj.invoke(full_path)
    
    
    # Core - Models
    obj = DjGenerateCoreModels()
    obj.invoke(full_path)
    
    
    # Home Page
    obj = DjGeneratePageHome()
    obj.invoke(full_path, project_name_format, app_main)
    
    
    
    # Module - User
    obj = DjGenerateModuleUsers()
    obj.invoke(full_path, project_name, project_name_format, app_main, domain_name)
    

    # Module - Auth
    obj = DjGenerateModuleAuth()
    obj.invoke(full_path)
    
    
    # Djangorestframework Json API
    obj = DjGenerateDjangorestframeworkJsonapi()
    obj.invoke(full_path, venv_python, app_main)
    
    
    # Module - Devs
    obj = DjGenerateModuleDevs()
    obj.invoke(full_path, project_name_format, app_main, venv_python)
    
    
    # CronJobs
    obj = DjGenerateCron()
    obj.invoke(full_path, project_name_format, app_main, venv_python)
    
    
    obj = DjGenerateCustomLogging()
    obj.invoke(full_path, project_name_format, app_main, venv_python)
    
    
    
    # TODO
    obj = DjGeneratePostman()
    obj.invoke(full_path, project_name, domain_name)
    
    
    
    obj = DjGenerateRequirementsTxt()
    obj.invoke(full_path, venv_python)
    
    
    obj = DjGenerateApiResponse()
    obj.invoke(full_path)
    

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
    from gen.php_laravel.to_create_project.auth.generate_module_auth import (
        generate_module_auth as generate_php_module_auth,
    )
    from gen.php_laravel.to_create_project.batch_processes.generate_batch_processes import (
        generate_batch_processes,
    )
    from gen.php_laravel.to_create_project.dashboards.generate_dashboard import (
        generate_dashboard,
    )
    from gen.php_laravel.to_create_project.dev.generate_execute_controller import (
        generate_execute_controller,
    )
    from gen.php_laravel.to_create_project.dev.generate_route_test import generate_route_test
    from gen.php_laravel.to_create_project.dev.generate_test_controller import (
        generate_test_controller,
    )
    from gen.php_laravel.to_create_project.excel.generate_maatwebsite_excel import (
        generate_maatwebsite_excel,
    )
    from gen.php_laravel.to_create_project.fpdf_merge.generate_fpdf_merge import (
        generate_fpdf_merge,
    )
    from gen.php_laravel.to_create_project.generate_by_command_line import (
        generate_by_command_line as generate_php_by_command_line,
    )
    from gen.php_laravel.to_create_project.generate_enums import generate_enums
    from gen.php_laravel.to_create_project.images.generate_company_logos import (
        generate_company_logos,
    )
    from gen.php_laravel.to_create_project.scripts.generate_shared_postman_collections import (
        generate_shared_postman_collections,
    )
    from gen.php_laravel.to_create_project.shared.generate_shared import generate_shared
    from gen.php_laravel.to_create_project.snappy.generate_snappy import generate_snappy
    from gen.php_laravel.to_create_project.updates.update_app_php import update_app_php
    from gen.php_laravel.to_create_project.updates.update_bootstrap_app_php import (
        update_bootstrap_app_php,
    )
    from gen.php_laravel.to_create_project.updates.update_gitignore import update_gitignore
    from gen.php_laravel.to_create_project.updates.update_model_user_php import (
        update_model_user,
    )
    from gen.php_laravel.to_create_project.updates.update_readme import update_readme
    from gen.php_laravel.to_create_project.updates.update_route_api_php import (
        update_route_api_php,
    )
    from gen.php_laravel.to_create_project.updates.update_welcome_blade import (
        update_welcome_blade,
    )
    from gen.php_laravel.to_create_project.updates.update_database import (
        update_database,
    )
    
    from gen.php_laravel.to_create_project.updates.update_envs import (
        update_envs,
    )
    from gen.php_laravel.to_create_project.utilities.generate_utilities import (
        generate_utilities,
    )
    
    from gen.php_laravel.to_create_project.exceptions.generate_exception_handler_response import (
        generate_exception_handler_response
    )

    full_path = _full_path(project_path, project_name)
    
    domain_name = helper_domain.helper_domain_name(project_name)
    
    password = os.getenv("PASSWORD")
    
    
    generate_php_by_command_line(full_path)
    generate_snappy(full_path)
    generate_fpdf_merge(full_path)
    generate_maatwebsite_excel(full_path)
    generate_enums(full_path, project_name, domain_name, password)
    generate_batch_processes(full_path)
    generate_default_role_permissions(full_path)
    generate_trait_api_response(full_path)
    generate_trait_tracks_users(full_path)
    generate_php_module_auth(full_path)
    update_route_api_php(full_path)
    generate_shared(full_path)
    generate_dashboard(full_path)
    generate_utilities(full_path)
    update_model_user(full_path)
    update_role_user_model(full_path)
    update_ability_user_model(full_path)
    update_app_php(full_path)
    update_bootstrap_app_php(full_path)
    update_readme(full_path)
    update_gitignore(full_path)
    generate_execute_controller(full_path)
    generate_test_controller(full_path)
    generate_route_test(full_path)
    generate_company_logos(full_path)
    update_welcome_blade(full_path, project_name, domain_name)
    generate_shared_postman_collections(full_path, project_name, domain_name, password)
    update_database(full_path)
    update_envs(full_path, project_name, domain_name)
    generate_exception_handler_response(full_path)
    generate_query_filter(full_path)
    generate_test_mail(full_path)
    generate_base_api_request(full_path)
    generate_api_controller(full_path)
    update_app_service_provider(full_path)
    

    return {
        "generator": "php_project",
        "project_name": project_name,
        "full_path": full_path,
    }
