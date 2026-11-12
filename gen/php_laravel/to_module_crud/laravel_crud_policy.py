
import os

from helpers.helper_file import HelperFile
from gen.helpers.helper_print import print_message, GREEN, CYAN


class LaravelCrudPolicy:

    def invoke(
        self,
        full_path,
        namespace,
        version_api,
        project_name,
        folder_group,
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
        Genera la Policy y actualiza AppServiceProvider.php.
        """

        folder_path = os.path.join(
            full_path,
            "app",
            "Policies",
            version_api,
            plural_name
        )

        path_use_model = (
            f"use App\\Models\\{namespace}\\"
            f"{plural_name}\\{singular_name};"
        )

        # Only model User
        if singular_name == "User":
            path_use_model = ""

        content = f"""<?php

namespace App\\Policies\\{version_api}\\{plural_name};

{path_use_model}
use App\\Permissions\\V1\\{plural_name}\\{singular_name}Permission;
use App\\Models\\User;


class {singular_name}Policy
{{
    /**
     * Create a new policy instance.
     */
    public function __construct(){{ }}
    public function viewAny(User $user): bool
    {{
        return $user->tokenCan('*')
            || $user->tokenCan({singular_name}Permission::INDEX);
    }}
    public function index(User $user): bool
    {{
        return $user->tokenCan('*')
            || $user->tokenCan({singular_name}Permission::INDEX);
    }}
    public function show(User $user, {singular_name} $model): bool
    {{
        return $user->tokenCan('*')
            || $user->tokenCan({singular_name}Permission::SHOW);
    }}

    public function store(User $user): bool
    {{
        return $user->tokenCan('*')
            || $user->tokenCan({singular_name}Permission::STORE);
    }}


    public function update(User $user, {singular_name} $model)
    {{
        if ($user->tokenCan('*')) {{
            return true;
        }}

        if ($user->tokenCan({singular_name}Permission::UPDATE)) {{
            return true;
        }}

        if ($user->tokenCan({singular_name}Permission::UPDATE_OWN)) {{
            return $user->id === $model->created_by;
        }}

        return false;
    }}
    public function delete(User $user, {singular_name} $model): bool
    {{
        if ($user->tokenCan('*')) {{
            return true;
        }}

        if ($user->tokenCan({singular_name}Permission::DELETE)) {{
            return true;
        }}

        if ($user->tokenCan({singular_name}Permission::DELETE_OWN)) {{
            return $user->id === $model->created_by;
        }}

        return false;
    }}
}}
"""

        # Crear archivo Policy
        HelperFile.write(
            folder_path=folder_path,
            file_name=f"{singular_name}Policy.php",
            content=content
        )

        # Actualizar AppServiceProvider.php
        self.update_app_service_provider(
            full_path,
            namespace,
            version_api,
            singular_name,
            plural_name
        )






    def update_app_service_provider(
        self,
        full_path,
        namespace,
        version_api,
        singular_name,
        plural_name
    ):
        """
        Actualiza AppServiceProvider.php.
        """

        main_path = os.path.join(
            full_path,
            "app",
            "Providers",
            "AppServiceProvider.php"
        )

        if not os.path.exists(main_path):
            print_message(
                f"Error: {main_path} no existe.",
                CYAN
            )
            return

        try:
            with open(main_path, "r", encoding="utf-8") as f:
                content = f.read()

            path_temp = (
                f"App\\Models\\{namespace}\\"
                f"{plural_name}\\{singular_name}"
            )

            # Only model User
            if singular_name == "User":
                path_temp = "App\\Models\\User"

            model_import = f"use {path_temp};"

            policy_import = (
                f"use App\\Policies\\{version_api}\\"
                f"{plural_name}\\{singular_name}Policy;"
            )

            policy_register = (
                f"Gate::policy("
                f"{singular_name}::class, "
                f"{singular_name}Policy::class);"
            )

            # Añadir import del modelo
            if model_import not in content:
                content = content.replace(
                    "use Illuminate\\Support\\ServiceProvider;",
                    f"""{model_import}
use Illuminate\\Support\\ServiceProvider;"""
                )

            # Añadir import de la Policy
            if policy_import not in content:
                content = content.replace(
                    "use Illuminate\\Support\\ServiceProvider;",
                    f"""{policy_import}
use Illuminate\\Support\\ServiceProvider;"""
                )

            # Registrar Policy
            if policy_register not in content:
                content = content.replace(
                    """    public function boot(): void
    {""",
                    f"""    public function boot(): void
    {{
        // {singular_name}
        {policy_register}
"""
                )

            # Guardar archivo actualizado
            with open(main_path, "w", encoding="utf-8") as f:
                f.write(content)

            print_message(
                f"{main_path} actualizado correctamente.",
                GREEN
            )

        except Exception as e:
            print_message(
                f"Error al actualizar {main_path}: {e}",
                CYAN
            )
