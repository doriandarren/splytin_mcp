import os
from datetime import datetime
from helpers.helper_file import HelperFile
from helpers.helper_columns import HelperColumns
from gen.php_laravel.to_module_crud.helpers.helper_laravel_migrate import HelperLaravelMigrate


class LaravelCrudMigration:

    def invoke(
        self,
        full_path,
        namespace,
        version_api,
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
        Genera el archivo de migración de Laravel.
        """

        folder_path = os.path.join(
            full_path, "database", "migrations"
        )

        current_time = datetime.now().strftime("%Y_%m_%d_%H%M%S")

        file_name = (
            f"{current_time}_create_{plural_name_snake}_table.php"
        )

        migration_content = f"""<?php

use Illuminate\\Database\\Migrations\\Migration;
use Illuminate\\Database\\Schema\\Blueprint;
use Illuminate\\Support\\Facades\\Schema;

return new class extends Migration
{{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {{
        if (!Schema::connection('{namespace.lower()}')->hasTable('{plural_name_snake}')) {{

            Schema::connection('{namespace.lower()}')->create('{plural_name_snake}', function (Blueprint $table) {{

                $table->id();
"""

        # ================== UP: columnas ==================
        for column in columns:

            name = column["name"]
            is_fk = column.get("is_fk") or column.get("type") == "fk"

            if is_fk:

                table_name = column.get("related_table")

                if not table_name:
                    table_name = HelperColumns.pluralize(
                        name.removesuffix("_id")
                    )

                migration_content += HelperLaravelMigrate.php_column_line(column)

                migration_content += (
                    f"                $table->foreign('{name}')"
                    f"->references('id')->on('{table_name}')->onDelete('cascade');\n"
                )

            else:
                migration_content += HelperLaravelMigrate.php_column_line(column)

        migration_content += """
                $table->timestamps();
                $table->softDeletes();
                $table->userstamps();
            });
        }
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
"""

        # ================== DOWN: eliminar FKs ==================
        for column in columns:

            name = column["name"]
            is_fk = column.get("is_fk") or column.get("type") == "fk"

            if is_fk:

                migration_content += f"""        if (Schema::connection('{namespace.lower()}')->hasColumn('{plural_name_snake}', '{name}')) {{
            Schema::connection('{namespace.lower()}')->table('{plural_name_snake}', function (Blueprint $table) {{
                $table->dropForeign(['{name}']);
                $table->dropColumn('{name}');
            }});
        }}
"""

        migration_content += f"""        Schema::connection('{namespace.lower()}')->dropIfExists('{plural_name_snake}');
    }}
}};
"""

        # ================== Crear archivo ==================
        HelperFile.write(
            folder_path=folder_path,
            file_name=file_name,
            content=migration_content
        )