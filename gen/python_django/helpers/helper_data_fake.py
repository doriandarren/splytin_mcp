from gen.helpers.helper_columns import parse_columns_input
from gen.python_django.to_create_module_crud.standard_module_crud_python_django import standard_module_crud_python_django


class HelperDataFake:
    """
        Only Test
    """
    
    def __init__(self):
        pass
    
    
    @staticmethod
    def createCRUD(full_path: str, app_main: str) -> None:
        
        singular_name = "AiPromptCategory"
        plural_name = "AiPromptCategories"
        columns = parse_columns_input("name description slug")
        
        standard_module_crud_python_django(
            full_path,
            app_main,
            singular_name,
            plural_name,
            columns
        )
        
        
        singular_name = "AiPromptGeneration"
        plural_name = "AiPromptGenerations"
        columns = parse_columns_input("ai_prompt_category_id:fk system_role system_message user_role user_message is_text_processed:boolean is_image_processed:boolean is_video_processed:boolean")
        standard_module_crud_python_django(
            full_path,
            app_main,
            singular_name,
            plural_name,
            columns
        )
    
    