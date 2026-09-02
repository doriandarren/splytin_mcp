import os
from gen.helpers.helper_print import print_message, GREEN, CYAN



def generate_trait_api_response(full_path):
    create_trait_api_response(full_path)
    update_controller(full_path)





def create_trait_api_response(full_path):
    """
    Genera el archivo
    """

    folder_path = os.path.join(full_path, "app", "Traits")
    file_path = os.path.join(folder_path, "ApiResponses.php")

    os.makedirs(folder_path, exist_ok=True)

    content = """<?php

namespace App\\Traits;

use App\\Enums\\Roles\\EnumRole;
use Illuminate\\Http\\JsonResponse;


trait ApiResponses
{

    private $message;
    private $code;
    

    public function getMessage()
    {
        return $this->message;
    }

    public function setMessage(string $message)
    {
        $this->message = $message;
    }

    public function getCode()
    {
        return $this->code;
    }

    public function setCode(int $code)
    {
        $this->code = $code;
    }

    /**
     * Respond Base
     * @param $data
     * @param array $headers
     * @return JsonResponse
     */
    public function respond($data, $headers = []){
        return response()->json(
            $data, 
            $this->getCode(),
            $headers
        );
    }

    /**
     * Respond Base with ERROR
     * @param string $message
     * @param null $errors
     * @param int $code
     * @return JsonResponse
     */
    public function respondWithError(
        string $message = '',
        $errors = null,
        int $code = 422
    ): JsonResponse {
        $this->setCode($code);

        return $this->respond([
            'data' => null,
            'message' => $message,
            'errors' => $errors,
            'success' => false,
            'status_code' => $code,
        ]);
    }

    /*************************************
     *  RESPONSE 200
     *************************************/
     
    /**
     * Respond with data
     *
     * @param null $message
     * @param null $data
     * @param bool $success
     * @return JsonResponse
     */
    public function respondWithData($message = null, $data = null, $success = true): JsonResponse
    {
        $this->setCode(200);
        return $this->respond([
            'data' => $data,
            'message' => $message,
            'status_code' => 200,
            'success' => $success,
        ]);
    }

    /**
     * Response with pagination data
     *
     * @param $message
     * @param $resource
     * @param $paginator
     * @param boolean $success
     * @return JsonResponse
     */
    public function respondWithPaginatedData(
        $message,
        $resource,
        $paginator,
        $success = true
    ): JsonResponse {
        $this->setCode(200);

        return $this->respond([
            'data' => $resource,

            'meta' => [
                'current_page' => $paginator->currentPage(),
                'per_page' => $paginator->perPage(),
                'last_page' => $paginator->lastPage(),
                'total' => $paginator->total(),
                'from' => $paginator->firstItem(),
                'to' => $paginator->lastItem(),
            ],

            'links' => [
                'first' => $paginator->url(1),
                'last' => $paginator->url($paginator->lastPage()),
                'prev' => $paginator->previousPageUrl(),
                'next' => $paginator->nextPageUrl(),
            ],

            'message' => $message,
            'status_code' => 200,
            'success' => $success,
        ]);
    }
    
    
    /**
    * Respond with Token
    *
    * @param string $message
    * @param string $token
    * @param mixed|null $user
    * @return JsonResponse
    */
    public function respondWithToken(
        string $message,
        string $token,
        $user = null
    ): JsonResponse {
        $this->setCode(200);

        $response = [
            'data' => [
                'token' => $token,
                'token_type' => 'Bearer',
            ],
            'message' => $message,
            'status_code' => 200,
            'success' => true,
        ];

        if ($user !== null) {
            $response['user'] = $user;
        }

        return $this->respond($response);
    }
    
    
    

    /*************************************
     *  RESPONSE 400
     *************************************/

    public function respondHttpBadRequest($message = 'Bad Request')
    {
        return $this->respondWithError(
            $message,
            ['e' => $message],
            400
        );
    }

    public function respondHttpUnauthorized($message = 'Unauthorized')
    {
        return $this->respondWithError(
            $message,
            ['e' => $message],
            401
        );
    }

    public function respondHttpConflict($message = 'Data Conflict')
    {
        return $this->respondWithError(
            $message,
            ['e' => $message],
            409
        );
    }

    public function respondUnprocessableEntity($message = 'Unprocessable Entity')
    {
        return $this->respondWithError(
            $message,
            ['e' => $message],
            422
        );
    }
    

    /**
     * Role Admin
     * @param $roles
     * @return bool
     */
    protected function isAdmin($roles): bool
    {
        foreach ($roles as $role) {
            if($role->name == EnumRole::ADMIN){
                return true;
            }
        }
        return false;
    }


    /**
     * Role Manager
     * @param $roles
     * @return bool
     */
    protected function isManager($roles): bool
    {
        foreach ($roles as $role) {

            if($role->name == EnumRole::MANAGER){
                return true;
            }

//            if($role->name == EnumRole::TRAFFIC_CHIEF){
//                return true;
//            }

            if($role->name == EnumRole::ERP){
                return true;
            }
        }
        return false;
    }




    /**
     * Role Staff
     * @param $roles
     * @return bool
     */
    protected function isUser($roles): bool
    {
        foreach ($roles as $role) {

            if($role->name == EnumRole::USER){
                return true;
            }

        }
        return false;
    }


//    /**
//     * Role Driver
//     * @param $roles
//     * @return bool
//     */
//    protected function isDriver($roles): bool
//    {
//        foreach ($roles as $role) {
//
//            if($role->name == EnumRole::DRIVER){
//                return true;
//            }
//
//        }
//        return false;
//    }

}
"""

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print_message(f"Archivo generado: {file_path}", GREEN)
    except Exception as e:
        print_message(f"Error al generar el archivo {file_path}: {e}", CYAN)
        
        
        
        
        
        



        





def update_controller(full_path):
    """
    Actualiza el archivo config/app.php
    """

    main_path = os.path.join(full_path, "app", "Http", "Controllers", "Controller.php")

    # Verificar si el archivo existe
    if not os.path.exists(main_path):
        print_message(f"Error: {main_path} no existe.", CYAN)
        return

    try:
        # Leer el contenido del archivo
        with open(main_path, "r") as f:
            content = f.read()
            
        

        # Reemplazos
        content = content.replace(
            """namespace App\Http\Controllers;""",
            """namespace App\Http\Controllers;

use App\Traits\ApiResponses;"""
        )
        
        
        # Reemplazos
        content = content.replace(
            """}""",
            """    use ApiResponses;
}"""
        )

        # Escribir el contenido actualizado
        with open(main_path, "w") as f:
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
        
       
