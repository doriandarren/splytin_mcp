
from helpers.helper_file import HelperFile
from gen.php_laravel.to_module_crud.helpers.helper_laravel_model import HelperLaravelModel


class LaravelCrudModel:

    def invoke(
        self,
        full_path,
        namespace,
        singular_name,
        plural_name,
        plural_name_snake,
        columns
    ):
        """
        Genera el archivo.
        """

        folder_path = HelperLaravelModel.get_folder_path(
            full_path,
            namespace,
            plural_name
        )

        relation_uses = HelperLaravelModel.format_relation_uses(
            namespace,
            columns
        )

        relation_fields = HelperLaravelModel.format_relation_fields(
            columns
        )

        # Preparar los campos fillable
        fillable = ",\n        ".join(
            f"'{column['name']}'"
            for column in columns
        )

        content = f"""<?php

namespace App\\Models\\{namespace}\\{plural_name};

use Illuminate\\Database\\Eloquent\\Factories\\HasFactory;
use Illuminate\\Database\\Eloquent\\Model;
use Illuminate\\Database\\Eloquent\\Builder;
use App\\Traits\\TracksUsers;
use App\\Http\\Filters\\V1\\QueryFilter;
{relation_uses}

class {singular_name} extends Model
{{
    use HasFactory;
    use TracksUsers;
    // use SoftDeletes;

    protected $connection = '{namespace.lower()}';
    protected $table = '{plural_name_snake}';
"""

        content += f"""    protected $fillable = [
        {fillable}
    ];

"""

        content += f"""
    /************************
    * Scope Filter
    ************************/
    public function scopeFilter(Builder $builder, QueryFilter $filters)
    {{
        return $filters->apply($builder);
    }}

    /************************
    * RELATIONS
    ************************/
{relation_fields}

    // TODO add relation tables
    // public function classrelacion()
    // {{
    //     return $this->hasMany(Relation::class, 'relacion_id', 'id');
    // }}
}}
"""

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name=f"{singular_name}.php",
            content=content
        )
