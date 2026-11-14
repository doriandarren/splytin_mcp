import os
from gen.php_laravel.to_module_crud.standard_module_crud_php import standard_module_crud_php
from helpers.helper_columns import HelperColumns
from helpers.helper_print import print_green, print_red




class LaravelDashboard:

    def invoke(self, full_path):
        
        self.create_module(full_path)
        
        
        
        self.create_list_controller(full_path)
        self.create_router(full_path)
        self.create_service(full_path)



    def create_list_controller(self, full_path):
        """
        Genera el archivo
        """

        folder_path = os.path.join(full_path, "app", "Http", "Controllers", "API", "V1", "Dashboards")
        file_path = os.path.join(folder_path, "DashboardIndexController.php")

        os.makedirs(folder_path, exist_ok=True)

        content = r'''<?php

namespace App\Http\Controllers\API\V1\Dashboards;

use App\Http\Controllers\Api\V1\ApiController;
use Illuminate\Support\Facades\Auth;
use Illuminate\Http\Request;
use Illuminate\Http\JsonResponse;
use App\Services\V1\Dashboards\DashboardService;

class DashboardIndexController extends ApiController
{
    private DashboardService $repository;

    public function __construct()
    {
        $this->repository = new DashboardService();
    }

    /**
    * @header Authorization Bearer TOKEN
    *
    * @param Request $request
    * @return JsonResponse
    */
    public function __invoke(Request $request): JsonResponse
    {
        $data = [];

        if ($this->isAdmin(Auth::user()->roles)) {
            
            // By Admin
            $data = $this->repository->index();
            
        } elseif ($this->isManager(Auth::user()->roles)) {
            
            // By Manager
            $data = $this->repository->indexByRoleManager();
            
        } elseif ($this->isUser(Auth::user()->roles)) {
            
            // By User
            $data = $this->repository->indexByRoleUser();
            
        }

        return $this->respondWithData('Dashboards Index', $data);
    }
}

'''

        try:
            with open(file_path, "w") as f:
                f.write(content)
            print_green(f"Archivo generado: {file_path}")
        except Exception as e:
            print_red(f"Error al generar el archivo {file_path}: {e}")



    def create_router(self, full_path):
        """
        Genera el archivo
        """

        folder_path = os.path.join(full_path, "routes", "API", "V1")
        file_path = os.path.join(folder_path, "dashboards.php")

        os.makedirs(folder_path, exist_ok=True)

        content = r'''<?php

// use App\Enums\EnumApiSetup;
// use App\Enums\EnumAbilitySuffix;

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\API\V1\Dashboards\DashboardIndexController;


/**
* Dashboards
*/
Route::group(['prefix' => 'dashboards/'], function () {

	Route::group(['middleware' => 'auth:sanctum'], function() {

		Route::get('/', [DashboardIndexController::class, '__invoke']);

	});
});

'''

        try:
            with open(file_path, "w") as f:
                f.write(content)
            print_green(f"Archivo generado: {file_path}")
        except Exception as e:
            print_red(f"Error al generar el archivo {file_path}: {e}")
    
    
        
    def create_service(self, full_path):
        """
        Genera el archivo
        """

        folder_path = os.path.join(full_path, "app", "Services", "V1", "Dashboards")
        file_path = os.path.join(folder_path, "DashboardService.php")

        os.makedirs(folder_path, exist_ok=True)

        content = r'''<?php

namespace App\Services\V1\Dashboards;

// use App\Enums\EnumApiSetup;

class DashboardService
{

    // const WITH = [];

    /**
    * List
    */
    public function index()
    {
        // TODO implement
        return [];
    }

    /**
    * List by manager
    */
    public function indexByRoleManager()
    {
        // TODO implement
        return [];
    }



    /**
    * List by user
    */
    public function indexByRoleUser()
    {
        // TODO implement
        return [];
    }

}
'''

        try:
            with open(file_path, "w") as f:
                f.write(content)
            print_green(f"Archivo generado: {file_path}")
        except Exception as e:
            print_red(f"Error al generar el archivo {file_path}: {e}")




    def create_module(self, full_path):
        
        ## By all:
        input_menu_checkbox = [
            "model",
            "controller_index",
            "controller_show",
            "controller_store",
            "controller_update",
            "controller_destroy",
            "service",
            "routes",
            "resource",
            "seeder",
            "factory",
            "postman",
            "migration",
        ]


        namespace = "API"
        folder_group = "SHARED"


        # Dashboard
        singular_name = "Dashboard"
        plural_name = "Dashboards"
        input_columns = "ability_group_id:fk name:unique label"

        columns = HelperColumns.parse_columns_input(input_columns)

        standard_module_crud_php(
            full_path=full_path,
            namespace=namespace,
            version_api='V1',
            folder_group=folder_group,
            singular_name=singular_name,
            plural_name=plural_name,
            columns=columns,
            input_menu_checkbox=input_menu_checkbox
        )
