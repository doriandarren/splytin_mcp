import os
from helpers.helper_file import HelperFile
from helpers.helper_print import dd, print_green, print_red, run_command


class ReactTsI18n:

    def invoke(self, full_path):
        self.install(full_path)
        self.create_index_ts(full_path)
        self.create_es_common_json(full_path)
        self.create_en_common_json(full_path)
        self.update_main_tsx(full_path)
        
    
    
    def install(self, full_path):
        # Instalar dependencias
        run_command(
            "npm install i18next react-i18next i18next-browser-languagedetector",
            cwd=full_path
        )

        print_green("i18next creado correctamente.")
        
        
    
    def create_index_ts(self, full_path):
        """
        Genera el archivo.
        """
    
        folder_path = os.path.join(full_path, "src", "i18n")
    
        content = r'''// src/i18n/index.ts
import i18n from "i18next";
import { initReactI18next } from "react-i18next";
import LanguageDetector from "i18next-browser-languagedetector";

import esCommon from "./locales/es/common.json";
import enCommon from "./locales/en/common.json";

import esAuth from "./locales/es/auth.json";
import enAuth from "./locales/en/auth.json";


const resources = {
    es: {
        common: esCommon,
        auth: esAuth,
    },
    en: {
        common: enCommon,
        auth: enAuth,
    },
};

i18n
    .use(LanguageDetector)
    .use(initReactI18next)
    .init({
        resources,
        fallbackLng: "es",
        supportedLngs: ["es", "en"],

        defaultNS: "common",
        ns: ["common", "auth"],

        detection: {
            order: ["localStorage", "navigator"],
            caches: ["localStorage"],
            lookupLocalStorage: "erp_language",
        },

        interpolation: {
            escapeValue: false,
        },
    });

export default i18n;
'''
    
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="index.ts",
            content=content
        )
        
        
    
    def create_es_common_json(self, full_path):
        """
        Genera el archivo.
        """
    
        folder_path = os.path.join(full_path, "src", "i18n", "locales", "es")
    
        content = r'''{
    "app_name": "Sistema de Gestión Empresarial",
    "dashboard": "Panel de control",
    "systems": "Sistemas",
    "customers": "Clientes",
    "washes": "Lavados",
    "settings": "Configuración",
    "logout": "Cerrar sesión",
    "save": "Guardar",
    "cancel": "Cancelar",
    "delete": "Eliminar",
    "edit": "Editar",
    "create": "Crear",
    "loading": "Cargando..."
}'''
    
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="common.json",
            content=content
        )
    
    
    
    def create_en_common_json(self, full_path):
        """
        Genera el archivo.
        """
    
        folder_path = os.path.join(full_path, "src", "i18n", "locales", "en")
    
        content = r'''{
    "app_name": "Business Management System",
    "dashboard": "Dashboard",
    "systems": "Systems",
    "customers": "Customers",
    "washes": "Washes",
    "settings": "Settings",
    "logout": "Log out",
    "save": "Save",
    "cancel": "Cancel",
    "delete": "Delete",
    "edit": "Edit",
    "create": "Create",
    "loading": "Loading..."
}'''
    
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="common.json",
            content=content
        )



    def create_es_auth_json(self, full_path):
        """
        Genera el archivo.
        """
    
        folder_path = os.path.join(full_path, "src", "i18n", "locales", "en")
    
        content = r'''# 
    '''
    
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="auth.json",
            content=content
        )
        
    
    def create_en_auth_json(self, full_path):
        """
        Genera el archivo.
        """
    
        folder_path = os.path.join(full_path, "src", "i18n", "locales", "es")
    
        content = r'''# 
    '''
    
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="auth.json",
            content=content
        )




    def update_main_tsx(self, full_path):
        """
        Actualiza el archivo
        """
        main_path = os.path.join(full_path, "src", "main.tsx")
    
        # Verificar si el archivo existe
        if not os.path.exists(main_path):
            print_red(f"Error: {main_path} no existe.")
            dd(f"Error: {main_path} no existe.")
            return False
    
        try:
            # Leer el contenido del archivo
            with open(main_path, "r", encoding="utf-8") as f:
                content = f.read()
    
            # Reemplazos
            replacements = {
                ## New Item -> KEY : VALUE
                """import { App } from './App';""":
                """import "@/i18n";
import { App } from './App';""",
            }
    
            # Validar y aplicar los reemplazos
            new_content = content
    
            for old_text, new_text in replacements.items():
                if old_text not in new_content:
                    raise ValueError(f"No se encontró el texto esperado: {old_text}")
    
                new_content = new_content.replace(old_text, new_text, 1)
    
            if new_content == content:
                raise ValueError("No se realizó ningún reemplazo.")
    
            # Escribir el contenido actualizado
            with open(main_path, "w", encoding="utf-8") as f:
                f.write(new_content)
    
            print_green(f"{main_path} actualizado correctamente.")
    
            return True
    
        except Exception as e:
            print_red(f"Error al actualizar {main_path}: {e}")
            return False
    
        
    
    
    