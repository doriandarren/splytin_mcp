import os
from gen.helpers.helper_print import print_message, GREEN, CYAN



def generate_dashboard(full_path):
    create_router(full_path)
    create_list_controller(full_path)
    create_service(full_path)



def create_list_controller(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "app", "Http", "Controllers", "API", "V1", "Dashboards")
    file_path = os.path.join(folder_path, "DashboardIndexController.php")

    os.makedirs(folder_path, exist_ok=True)

    content = r'''<?php

namespace App\Http\Controllers\API\V1\Dashboards;

use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use App\Http\Controllers\Controller;
use App\Services\API\V1\Dashboards\DashboardService;

class DashboardIndexController extends Controller
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
            $data = $this->repository->index();
        } elseif ($this->isManager(Auth::user()->roles)) {
            $data = $this->repository->indexByRoleManager();
        } elseif ($this->isUser(Auth::user()->roles)) {
            $data = $this->repository->indexByRoleUser();
        }

        return $this->respondWithData('Dashboards Index', $data);
    }
}

'''

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
        
        
        

        
def create_router(full_path):
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
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
        
        
        
        
        
        




        
def create_service(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "app", "Services", "API", "V1", "Dashboards")
    file_path = os.path.join(folder_path, "DashboardService.php")

    os.makedirs(folder_path, exist_ok=True)

    content = r'''<?php

namespace App\Services\API\V1\Dashboards;

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
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
