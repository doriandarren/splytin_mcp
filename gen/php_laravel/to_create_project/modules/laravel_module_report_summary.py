from gen.php_laravel.to_module_crud.standard_module_crud_php import standard_module_crud_php
from helpers.helper_columns import HelperColumns




class LaravelModuleReportSummary:

    def invoke(self, full_path):
        
        self.create_module(full_path)


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


        # Report Summary
        singular_name = "ReportSummary"
        plural_name = "ReportSummaries"
        input_columns = "total_customers:int total_invoices:int total_income:decimal total_expenses:decimal"

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
