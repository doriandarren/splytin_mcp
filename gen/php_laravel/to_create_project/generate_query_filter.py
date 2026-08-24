import os
from gen.helpers.helper_print import print_message, GREEN, CYAN

def generate_query_filter(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "app", "Http", "Filters", "API", "V1")
    file_path = os.path.join(folder_path, "QueryFilter.php")

    os.makedirs(folder_path, exist_ok=True)

    content = r'''<?php

namespace App\Http\Filters\API\V1;

use Illuminate\Database\Eloquent\Builder;
use Illuminate\Http\Request;

abstract class QueryFilter
{
    protected $builder;
    protected $request;
    protected $sortable = [];


    public function __construct(Request $request)
    {
        $this->request = $request;
    }




    public function apply(Builder $builder)
    {
        $this->builder = $builder;


        foreach ($this->request->all() as $key => $value) {
            if (method_exists($this, $key)) {
                $this->$key($value);
            }
        }


        return $builder;
    }



    protected function filter($arr)
    {

        foreach ($arr as $key => $value) {
            if (method_exists($this, $key)) {
                $this->$key($value);
            }
        }

        $this->builder;

    }


    protected function sort($value)
    {
        $sortAttributes = explode(',', $value);

        foreach ($sortAttributes as $sortAttribute) {

            $direction = 'asc';

            if(strpos($sortAttribute, '-') === 0){
                $direction = 'desc';
                $sortAttribute = substr($sortAttribute, 1);
            }

            if(!in_array($sortAttribute, $this->sortable) && !array_key_exists($sortAttribute, $this->sortable)){
                continue;
            }

            $columnName = $this->sortable[$sortAttribute] ?? null;

            if($columnName === null){
                $columnName = $sortAttribute;
            }

            $this->builder->orderBy($columnName, $direction);

        }

    }

}
'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
