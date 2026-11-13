import os
from helpers.helper_file import HelperFile
from helpers.helper_print import dd, print_green, print_red, run_command


class ReactTsI18n:

    def invoke(self, full_path):
        self.install(full_path)
        self.create_index_ts(full_path)
        self.create_es_common_json(full_path)
        self.create_en_common_json(full_path)
        self.create_en_auth_json(full_path)
        self.create_es_auth_json(full_path)
        self.update_main_tsx(full_path)
        self.create_component_language_selector_tsx(full_path)
        
    
    
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
    "quotes": "Presupuestos",
    "teams": "Equipos",
    "settings": "Configuración",
    "auth": {
        "profile": "Perfil",
        "logout": "Cerrar sesión"
    },
    "actions": {
        "create": "Crear",
        "save": "Guardar",
        "edit": "Editar",
        "update": "Actualizar",
        "delete": "Eliminar",
        "cancel": "Cancelar",
        "close": "Cerrar",
        "search": "Buscar",
        "filter": "Filtrar",
        "refresh": "Actualizar datos",
        "back": "Volver",
        "confirm": "Confirmar"
    },
    "status": {
        "loading": "Cargando...",
        "success": "Operación realizada correctamente",
        "error": "Ha ocurrido un error",
        "no_results": "No se encontraron resultados"
    }
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
    "quotes": "Quotes",
    "teams": "Teams",
    "settings": "Settings",
    "auth": {
        "profile": "Profile",
        "logout": "Log out"
    },
    "actions": {
        "create": "Create",
        "save": "Save",
        "edit": "Edit",
        "update": "Update",
        "delete": "Delete",
        "cancel": "Cancel",
        "close": "Close",
        "search": "Search",
        "filter": "Filter",
        "refresh": "Refresh data",
        "back": "Back",
        "confirm": "Confirm"
    },
    "status": {
        "loading": "Loading...",
        "success": "Operation completed successfully",
        "error": "An error occurred",
        "no_results": "No results found"
    }
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
    
        content = r'''{
    "logo_alt": "Company logo",
    "app_title": "Business Management System",
    "app_subtitle": "ERP Edition",
    "login_title": "Sign in",
    "login_description": "Enter your credentials to access the system.",
    "email_label": "Email address",
    "email_placeholder": "Email",
    "password_label": "Password",
    "password_placeholder": "Password",
    "show_password": "Show password",
    "hide_password": "Hide password",
    "remember_me": "Remember me",
    "forgot_password": "Forgot your password?",
    "logging_in": "Signing in…",
    "submit": "Sign in",
    "terms_prefix": "By signing in, you agree to our",
    "terms_link": "Terms and Conditions",
    "terms_connector": "and our",
    "privacy_link": "Privacy Policy"
}'''
    
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
    
        content = r'''{
    "logo_alt": "Logo de la empresa",
    "app_title": "Sistema de Gestión Empresarial",
    "app_subtitle": "ERP Edition",
    "login_title": "Iniciar sesión",
    "login_description": "Introduce tus credenciales para acceder al sistema.",
    "email_label": "Correo electrónico",
    "email_placeholder": "Email",
    "password_label": "Contraseña",
    "password_placeholder": "Contraseña",
    "show_password": "Mostrar contraseña",
    "hide_password": "Ocultar contraseña",
    "remember_me": "Recordarme",
    "forgot_password": "¿Olvidaste tu contraseña?",
    "logging_in": "Iniciando sesión…",
    "submit": "Entrar",
    "terms_prefix": "Al iniciar sesión, aceptas nuestros",
    "terms_link": "Términos y condiciones",
    "terms_connector": "y nuestra",
    "privacy_link": "Política de privacidad"
}'''
    
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





    def create_component_language_selector_tsx(self, full_path):
        """
        Genera el archivo.
        """
    
        folder_path = os.path.join(full_path, "src", "components", "languages")
    
        content = r'''// src/components/languages/LanguageSelector.tsx
import { useTranslation } from "react-i18next";
import { Globe } from "lucide-react";

import {
    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
    SelectValue,
} from "@/components/ui/select";

interface LanguageSelectorProps {
    className?: string;
}

export function LanguageSelector({
    className = "w-36",
}: LanguageSelectorProps) {
    const { i18n } = useTranslation();

    const languages = [
        { value: "es", label: "Español" },
        { value: "en", label: "English" },
    ];

    const handleLanguageChange = (language: string| null) => {
        if(!language) return;
        void i18n.changeLanguage(language);
    };

    return (
        <Select
            value={i18n.resolvedLanguage ?? "es"}
            onValueChange={handleLanguageChange}
        >
            <SelectTrigger
                className={className}
                aria-label="Select language"
            >
                <Globe className="size-4" />
                <SelectValue placeholder="Idioma" />
            </SelectTrigger>

            <SelectContent>
                {languages.map((language) => (
                    <SelectItem
                        key={language.value}
                        value={language.value}
                    >
                        {language.label}
                    </SelectItem>
                ))}
            </SelectContent>
        </Select>
    );
}'''
    
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="LanguageSelector.tsx",
            content=content
        )


