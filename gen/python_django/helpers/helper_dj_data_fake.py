from helpers.helper_columns import HelperColumns
from gen.python_django.to_create_module_crud.standard_module_crud_python_django import StandardModuleCrudPythonDjango


class HelperDjDataFake:
    """
        Only Test
    """
    
    def __init__(self):
        self.module_crud = StandardModuleCrudPythonDjango()
        
    
    
    
    def invoke(self, full_path: str, app_main: str) -> None:
        
        ######################
        # AiPromptCategory
        ######################
        singular_name = "AiPromptCategory"
        plural_name = "AiPromptCategories"
        columns = HelperColumns.parse_columns_input(
            "name description slug"
        )
        
        self.module_crud.invoke(
            full_path,
            app_main,
            singular_name,
            plural_name,
            columns
        )
        
        
        ######################
        # AiPromptGeneration
        ######################
        singular_name = "AiPromptGeneration"
        plural_name = "AiPromptGenerations"
        columns = HelperColumns.parse_columns_input(
            "ai_prompt_category_id:fk system_role system_message user_role user_message is_text_processed:boolean is_image_processed:boolean is_video_processed:boolean"
        )
        
        self.module_crud.invoke(
            full_path,
            app_main,
            singular_name,
            plural_name,
            columns
        )
    
    