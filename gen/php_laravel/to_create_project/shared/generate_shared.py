import os
from gen.helpers.helper_columns import parse_columns_input
from gen.helpers.helper_print import print_message, GREEN, CYAN

from gen.php.to_create_project.shared.generate_migrations.generate_ability_groups_table import generate_ability_groups_table
from gen.php.to_create_project.shared.generate_migrations.generate_countries_table import generate_countries_table
from gen.php.to_create_project.shared.generate_migrations.generate_roles_table import generate_roles_table
from gen.php.to_create_project.shared.generate_migrations.update_create_users_table import update_create_users_table
from gen.php.to_create_project.shared.update_database_seeders.update_database_seeders import update_database_seeder
from gen.php.to_create_project.shared.user_roles_abilities.generate_seeder_user_roles_abilities import generate_seeder_user_roles_abilities
from gen.php.to_module_crud.standard_module_crud_php import standard_module_crud_php




def generate_shared(full_path):
    
    ## By all:
    input_menu_checkbox = [
        "model",
        "controller_list",
        "controller_show",
        "controller_store",
        "controller_update",
        "controller_destroy",
        "service",
        "routes",
        # "migration",
        "seeder",
        "factory",
        "postman",
    ]
    
    
    # Abilities
    namespace = "SHARED"
    singular_name = "Ability"
    plural_name = "Abilities"
    input_columns = "ability_group_id:fk name label"
    
    columns = parse_columns_input(input_columns)
    
    standard_module_crud_php(namespace, full_path, singular_name, plural_name, columns, input_menu_checkbox)
    
    
    
    # Abilities Groups
    namespace = "SHARED"
    singular_name = "AbilityGroup"
    plural_name = "AbilityGroups"
    input_columns = "name"
    
    columns = parse_columns_input(input_columns)
    
    standard_module_crud_php(namespace, full_path, singular_name, plural_name, columns, input_menu_checkbox)
    
    
    
    # Abilities Users
    namespace = "SHARED"
    singular_name = "AbilityUser"
    plural_name = "AbilityUsers"
    input_columns = "ability_group_id:fk user_id:fk"
    
    columns = parse_columns_input(input_columns)
    
    standard_module_crud_php(namespace, full_path, singular_name, plural_name, columns, input_menu_checkbox)
    
    
    # Countries
    namespace = "SHARED"
    singular_name = "Country"
    plural_name = "Countries"
    input_columns = "common_name iso_name code_alpha_2 code_alpha_3 numerical_code phone_code"
    
    columns = parse_columns_input(input_columns)
    
    standard_module_crud_php(namespace, full_path, singular_name, plural_name, columns, input_menu_checkbox)
    
    
    
    # Role Users
    namespace = "SHARED"
    singular_name = "RoleUser"
    plural_name = "RoleUsers"
    input_columns = "role_id:fk user_id:fk"
    
    columns = parse_columns_input(input_columns)
    
    standard_module_crud_php(namespace, full_path, singular_name, plural_name, columns, input_menu_checkbox)
    
    
    
    # Role
    namespace = "SHARED"
    singular_name = "Role"
    plural_name = "Roles"
    input_columns = "name description"
    
    columns = parse_columns_input(input_columns)
    
    standard_module_crud_php(namespace, full_path, singular_name, plural_name, columns, input_menu_checkbox)
    
    

    # User Statuses
    namespace = "SHARED"
    singular_name = "UserStatus"
    plural_name = "UserStatuses"
    input_columns = "name"
    
    columns = parse_columns_input(input_columns)
    
    standard_module_crud_php(namespace, full_path, singular_name, plural_name, columns, input_menu_checkbox)
    
    
    
    
    # UserRolesAbilities
    generate_seeder_user_roles_abilities(full_path)


    # Update DatabaseSeeder
    update_database_seeder(full_path)

    # Migrations
    update_create_users_table(full_path)
    generate_ability_groups_table(full_path)
    generate_roles_table(full_path)
    generate_countries_table(full_path)
    
    