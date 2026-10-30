import os
from gen.helpers.helper_file import HelperFile


class ReactTsModuleAuth:


    def invoke(self, full_path):
        self.create_file_auth_layout_tsx(full_path)
        self.create_file_login_page_tsx(full_path)
        self.create_file_register_page_tsx(full_path)
        
        self.create_service(full_path)
        self.create_type(full_path)
        
        
        self.create_auth_token_storage_ts(full_path)
        
        ## User Auth
        self.create_auth_user_types_ts(full_path)
        self.create_auth_user_service(full_path)
        
        
        #Protected Routes
        self.create_protected_route_tsx(full_path)
        self.create_auth_store_ts(full_path)
        
        # hooks
        self.create_hooks_use_auth_user(full_path)
        
        #queries
        self.create_auth_user_query_ts(full_path)
        
        # Utils
        self.create_auth_permissions_ts(full_path)



    def create_file_auth_layout_tsx(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "src", "modules", "auth", "layouts")

        content = r'''import { Outlet } from "react-router";

export const AuthLayout = () => {
  return (
    <>
      <Outlet />
    </>
  );
};
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="AuthLayout.tsx",
            content=content
        )
        
        
    def create_file_login_page_tsx(self, full_path):
        """
        Genera el archivo.
        """
    
        folder_path = os.path.join(full_path, "src", "modules", "auth", "login", "pages")
    
        content = r'''import { useEffect, useRef, useState } from "react";
import type { SubmitEvent } from "react";
import { Link, useLocation, useNavigate } from "react-router";

import {
  ArrowRight,
  Eye,
  EyeOff,
  LoaderCircle,
  PanelsTopLeft,
} from "lucide-react";

import { ApiError } from "@/api/api-error";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

import { authTokenStorage } from "../../services/authTokenStorage";
import { useAuthStore } from "../../stores/authStore";
import { login } from "../services/loginService";
import type { LoginRequest } from "../types/login.types";

type LoginFieldErrors = Partial<
  Record<keyof LoginRequest, string[]>
>;

export const LoginPage = () => {
  const navigate = useNavigate();
  const location = useLocation();

  // Zustand
  const setAuthenticated = useAuthStore(
    (state) => state.setAuthenticated
  );

  // Estados del formulario
  const [credentials, setCredentials] = useState<LoginRequest>({
    email: "admin@splytin.com",
    password: "Tailandia2026",
  });

  const [showPassword, setShowPassword] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");
  const [fieldErrors, setFieldErrors] = useState<LoginFieldErrors>({});

  // Control de peticiones
  const activeRequest = useRef<AbortController | null>(null);

  // Cancelar la petición al desmontar el componente
  useEffect(() => {
    return () => {
      activeRequest.current?.abort();
    };
  }, []);

  // Actualizar campos
  const updateField = (
    field: keyof LoginRequest,
    value: string
  ) => {
    setCredentials((previous) => ({
      ...previous,
      [field]: value,
    }));

    setFieldErrors((previous) => ({
      ...previous,
      [field]: undefined,
    }));

    setErrorMessage("");
  };

  // Enviar formulario
  const onSubmit = async (
    event: SubmitEvent<HTMLFormElement>
  ) => {
    event.preventDefault();

    // Evitar peticiones duplicadas
    if (activeRequest.current) return;

    const controller = new AbortController();
    activeRequest.current = controller;

    setIsSubmitting(true);
    setErrorMessage("");
    setFieldErrors({});

    try {
      // 1. Login contra Django
      const response = await login(
        {
          email: credentials.email.trim(),
          password: credentials.password,
        },
        controller.signal
      );

      if (controller.signal.aborted) return;

      // 2. Guardar el token
      try {
        authTokenStorage.set(response.data.attributes.token);
      } catch {
        setErrorMessage(
          "No se pudo guardar la sesión en este navegador. " +
          "Comprueba que el almacenamiento esté permitido."
        );
        return;
      }

      // 3. Actualizar autenticación en Zustand
      setAuthenticated(true);

      // 4. Limpiar formulario
      setCredentials({
        email: "",
        password: "",
      });

      // 5. Recuperar ruta original
      const from = location.state?.from;

      const destination =
        typeof from?.pathname === "string" &&
        from.pathname.startsWith("/admin") &&
        !from.pathname.startsWith("//")
          ? `${from.pathname}${from.search ?? ""}${from.hash ?? ""}`
          : "/admin";

      // 6. Redirigir
      void navigate(destination, { replace: true });

    } catch (error) {
      if (controller.signal.aborted) return;

      if (error instanceof ApiError) {
        const errors = error.getFieldErrors();

        setFieldErrors({
          email: errors.email,
          password: errors.password,
        });

        setErrorMessage(error.message);
      } else {
        setErrorMessage(
          "No se pudo iniciar sesión. Inténtalo de nuevo."
        );
      }
    } finally {
      activeRequest.current = null;

      if (!controller.signal.aborted) {
        setIsSubmitting(false);
      }
    }
  };

  return (
    <main className="grid min-h-svh bg-background lg:grid-cols-2">
      {/* Panel izquierdo */}
      <section className="hidden flex-col justify-between bg-slate-950 p-12 text-white lg:flex xl:p-20">
        <div className="flex items-center gap-3 text-xl font-semibold">
          <PanelsTopLeft
            aria-hidden="true"
            className="size-7"
          />

          <span>Splytin ERP</span>
        </div>

        <div className="max-w-lg space-y-6">
          <p className="text-sm font-medium uppercase tracking-widest text-slate-400">
            Tu espacio de trabajo
          </p>

          <h1 className="text-4xl font-semibold leading-tight xl:text-5xl">
            Todo lo que necesitas para gestionar tu empresa.
          </h1>

          <p className="text-lg leading-relaxed text-slate-300">
            Accede a tus herramientas y continúa donde lo dejaste.
          </p>
        </div>

        <p className="text-sm text-slate-400">
          Sistema de gestión empresarial
        </p>
      </section>

      {/* Panel derecho */}
      <section
        aria-labelledby="login-title"
        className="flex items-center justify-center px-6 py-12 sm:px-12"
      >
        <div className="w-full max-w-sm">
          {/* Logo móvil */}
          <div className="mb-10 flex items-center gap-2 font-semibold lg:hidden">
            <PanelsTopLeft
              aria-hidden="true"
              className="size-6"
            />
            Splytin ERP
          </div>

          {/* Título */}
          <div className="mb-8 space-y-2">
            <h2
              id="login-title"
              className="text-3xl font-semibold tracking-tight"
            >
              Iniciar sesión
            </h2>

            <p className="text-sm text-muted-foreground">
              Introduce tus credenciales para acceder al panel.
            </p>
          </div>

          {/* Formulario */}
          <form
            onSubmit={onSubmit}
            aria-busy={isSubmitting}
            className="space-y-5"
          >
            {/* Error general */}
            {errorMessage && (
              <div
                role="alert"
                className="rounded-lg border border-destructive/30 bg-destructive/5 p-3 text-sm text-destructive"
              >
                {errorMessage}
              </div>
            )}

            {/* Email */}
            <div className="space-y-2">
              <Label htmlFor="login-email">
                Correo electrónico
              </Label>

              <Input
                id="login-email"
                name="email"
                type="email"
                autoComplete="username"
                autoCapitalize="none"
                spellCheck={false}
                placeholder="tu@empresa.com"
                value={credentials.email}
                onChange={(event) =>
                  updateField("email", event.target.value)
                }
                required
                disabled={isSubmitting}
                aria-invalid={Boolean(
                  fieldErrors.email?.length
                )}
                aria-describedby={
                  fieldErrors.email?.length
                    ? "login-email-error"
                    : undefined
                }
                className="h-11"
              />

              {Boolean(fieldErrors.email?.length) && (
                <p
                  id="login-email-error"
                  className="text-sm text-destructive"
                >
                  {fieldErrors.email?.join(" ")}
                </p>
              )}
            </div>

            {/* Contraseña */}
            <div className="space-y-2">
              <Label htmlFor="login-password">
                Contraseña
              </Label>

              <div className="relative">
                <Input
                  id="login-password"
                  name="password"
                  type={showPassword ? "text" : "password"}
                  autoComplete="current-password"
                  value={credentials.password}
                  onChange={(event) =>
                    updateField(
                      "password",
                      event.target.value
                    )
                  }
                  required
                  disabled={isSubmitting}
                  aria-invalid={Boolean(
                    fieldErrors.password?.length
                  )}
                  aria-describedby={
                    fieldErrors.password?.length
                      ? "login-password-error"
                      : undefined
                  }
                  className="h-11 pr-12"
                />

                {/* Mostrar / ocultar contraseña */}
                <Button
                  type="button"
                  variant="ghost"
                  size="icon"
                  className="absolute right-1.5 top-1.5"
                  onClick={() =>
                    setShowPassword((previous) => !previous)
                  }
                  disabled={isSubmitting}
                  aria-label={
                    showPassword
                      ? "Ocultar contraseña"
                      : "Mostrar contraseña"
                  }
                  aria-pressed={showPassword}
                  aria-controls="login-password"
                >
                  {showPassword ? (
                    <EyeOff aria-hidden="true" />
                  ) : (
                    <Eye aria-hidden="true" />
                  )}
                </Button>
              </div>

              {Boolean(fieldErrors.password?.length) && (
                <p
                  id="login-password-error"
                  className="text-sm text-destructive"
                >
                  {fieldErrors.password?.join(" ")}
                </p>
              )}
            </div>

            {/* Botón */}
            <Button
              type="submit"
              disabled={isSubmitting}
              className="h-11 w-full"
            >
              {isSubmitting ? (
                <>
                  <LoaderCircle
                    aria-hidden="true"
                    className="animate-spin"
                  />
                  Iniciando sesión…
                </>
              ) : (
                <>
                  Entrar
                  <ArrowRight aria-hidden="true" />
                </>
              )}
            </Button>
          </form>

          {/* Volver al inicio */}
          <div className="mt-8 text-center">
            <Link
              to="/"
              className="text-sm text-muted-foreground underline-offset-4 hover:text-foreground hover:underline"
            >
              Volver al inicio
            </Link>
          </div>
        </div>
      </section>
    </main>
  );
};
'''
    
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="LoginPage.tsx",
            content=content
        )
    
    
    
    def create_file_register_page_tsx(self, full_path):
        """
        Genera el archivo.
        """
    
        folder_path = os.path.join(full_path, "src", "modules", "auth", "register", "pages")
    
    
        content = r'''export const RegisterPage = () => {
  return (
    <div>RegisterPage</div>
  )
}
'''
    
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="RegisterPage.tsx",
            content=content
        )
    
    
    
    def create_service(self, full_path):
        """
        Genera el archivo.
        """
    
        folder_path = os.path.join(full_path, "src", "modules", "auth", "login", "services")
    
        content = r'''import { api } from "@/api/api";
import { ApiError } from "@/api/api-error";

import type {
  LoginRequest,
  LoginResponse,
} from "../types/login.types";

/**
 * Comprueba que la respuesta del backend
 * contiene un token válido.
 */
function isLoginResponse(value: unknown): value is LoginResponse {
  if (!value || typeof value !== "object" || !("data" in value)) {
    return false;
  }

  const data = value.data;

  if (!data || typeof data !== "object") {
    return false;
  }

  if (!("type" in data) || data.type !== "auth-tokens") {
    return false;
  }

  if (
    !("attributes" in data) ||
    !data.attributes ||
    typeof data.attributes !== "object"
  ) {
    return false;
  }

  return (
    "token" in data.attributes &&
    typeof data.attributes.token === "string" &&
    data.attributes.token.trim().length > 0
  );
}

/**
 * Inicia sesión mediante la API de Django.
 *
 * - Envía las credenciales.
 * - No adjunta un token anterior.
 * - Valida la estructura de la respuesta.
 * - Devuelve el documento JSON:API completo.
 *
 * El almacenamiento del token se realiza
 * desde LoginPage mediante authTokenStorage.
 */
export async function login(
  credentials: LoginRequest,
  signal?: AbortSignal
): Promise<LoginResponse> {
  const response = await api<LoginResponse>("auth/login", {
    method: "POST",
    body: credentials,
    signal,
    contentType: "json",
    skipAuth: true,
  });

  if (!isLoginResponse(response)) {
    throw new ApiError(
      "La respuesta de login no contiene un token válido.",
      {
        kind: "invalid-response",
      }
    );
  }

  return response;
}
'''
    
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="loginService.ts",
            content=content
        )
    
    
    
    def create_type(self, full_path):
        """
        Genera el archivo.
        """
    
        folder_path = os.path.join(full_path, "src", "modules", "auth", "login", "types")
    
    
        content = r'''import type { JsonApiDocument } from "@/api/json-api.types";

export interface LoginRequest {
  email: string;
  password: string;
}

export interface AuthTokenResource {
  type: "auth-tokens";
  id?: string;
  attributes: {
    token: string;
  };
}

export type LoginResponse = JsonApiDocument<AuthTokenResource>;
'''
    
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="login.types.ts",
            content=content
        )
    
    
    
    
    
    def create_auth_token_storage_ts(self, full_path):
        """
        Genera el archivo.
        """
    
        folder_path = os.path.join(full_path, "src", "modules", "auth", "services")
    
    
        content = r'''// Clave propia de esta aplicación; el cliente HTTP no depende del almacenamiento.
const TOKEN_KEY = 'token_erp_ts_app1_com';

export const authTokenStorage = {
  get(): string | null {
    return localStorage.getItem(TOKEN_KEY);
  },
  set(token: string): void {
    localStorage.setItem(TOKEN_KEY, token);
  },
  clear(): void {
    localStorage.removeItem(TOKEN_KEY);
  },
};
'''
    
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="authTokenStorage.ts",
            content=content
        )


        
    def create_auth_user_types_ts(self, full_path):
        """
        Genera el archivo.
        """
    
        folder_path = os.path.join(full_path, "src", "modules", "auth", "types")
    
        content = r'''// auth/types/auth-user.types.ts
export interface AuthRole {
  type: string;
  id: number | string;
  attributes: {
    name: string;
    description: string | null;
    created_at: string;
    updated_at: string;
  };
}

export interface AuthUserStatus {
  type: string;
  id: number | string;
  attributes: {
    name: string;
    created_at: string;
    updated_at: string;
  };
}

export interface AuthUser {
  type: "auth";
  id: number | string;

  attributes: {
    user_status_id: number;
    name: string;
    email: string;
    image_url: string | null;
    created_at: string;
    updated_at: string;
  };

  relationships: {
    roles: AuthRole[];
    user_status: AuthUserStatus | null;
  };

  links?: {
    self?: string;
  };
}

export interface AuthUserResponse {
  data: AuthUser;
  message?: string;
  status_code?: number;
  success?: boolean;
}
'''
    
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="auth-user.types.ts",
            content=content
        )
    
    
    

    
    def create_auth_user_service(self, full_path):
        """
        Genera el archivo.
        """
    
        folder_path = os.path.join(full_path, "src", "modules", "auth", "services")
    
        content = r'''// auth/services/authUserService.ts
import { api } from "@/api/api";
import { ApiError } from "@/api/api-error";
import type { AuthUserResponse } from "../types/auth-user.types";

export const getAuthUser = async (
  signal?: AbortSignal
): Promise<AuthUserResponse> => {
  const response = await api<AuthUserResponse>("auth/user", {
    method: "GET",
    signal,
  });

  if (
    !response ||
    !response.data ||
    response.data.type !== "auth" ||
    !response.data.attributes ||
    typeof response.data.attributes.email !== "string"
  ) {
    throw new ApiError(
      "La respuesta del usuario autenticado no es válida.",
      { kind: "invalid-response" }
    );
  }

  return response;
};
'''
    
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="authUserService.ts",
            content=content
        )
    
    
    
    def create_protected_route_tsx(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "src", "modules", "auth", "components")

        content = r'''// auth/components/ProtectedRoute.tsx
import { useEffect } from "react";
import { Navigate, Outlet, useLocation } from "react-router";
import { useAuthStore } from "../stores/authStore";

export const ProtectedRoute = () => {
  const location = useLocation();

  const status = useAuthStore((state) => state.status);
  const checkSession = useAuthStore(
    (state) => state.checkSession
  );

  useEffect(() => {
    if (status === "checking") {
      void checkSession();
    }
  }, [status, checkSession]);

  if (status === "checking") {
    return (
      <div className="flex min-h-screen items-center justify-center">
        <p className="text-muted-foreground">
          Verificando sesión...
        </p>
      </div>
    );
  }

  if (status === "error") {
    return (
      <div className="flex min-h-screen flex-col items-center justify-center gap-4">
        <h2 className="text-xl font-semibold">
          No se pudo verificar la sesión
        </h2>

        <p className="text-sm text-muted-foreground">
          Comprueba tu conexión e inténtalo de nuevo.
        </p>

        <button
          type="button"
          className="rounded-md bg-primary px-4 py-2 text-primary-foreground"
          onClick={() => void checkSession()}
        >
          Reintentar
        </button>
      </div>
    );
  }

  if (status === "unauthenticated") {
    return (
      <Navigate
        to="/auth/login"
        replace
        state={{ from: location }}
      />
    );
  }

  return <Outlet />;
};
'''
        
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="ProtectedRoute.tsx",
            content=content
        )
        
        
        
        
    def create_auth_store_ts(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "src", "modules", "auth", "stores")

        content = r'''// auth/stores/authStore.ts

import { create } from "zustand";

import { ApiError } from "@/api/api-error";
import { queryClient } from "@/providers/QueryProvider";

import { authTokenStorage } from "../services/authTokenStorage";
import { authUserQuery } from "../queries/authUserQuery";

import type { AuthUser } from "../types/auth-user.types";

// Estados posibles de autenticación
type AuthStatus =
  | "checking"
  | "authenticated"
  | "unauthenticated"
  | "error";

interface AuthState {
  status: AuthStatus;
  isAuthenticated: boolean;
  user: AuthUser | null;

  setAuthenticated: (value: boolean) => void;
  checkSession: () => Promise<void>;
  logout: () => void;
}

// Evita peticiones duplicadas
let pendingCheck: Promise<void> | null = null;

// Identifica los cambios de sesión
let sessionVersion = 0;

// Limpia las consultas privadas de autenticación
function clearAuthQueries() {
  void queryClient.cancelQueries({
    queryKey: ["auth"],
  });

  queryClient.removeQueries({
    queryKey: ["auth"],
  });
}

export const useAuthStore = create<AuthState>((set, get) => ({
  // Al iniciar la aplicación comprobamos si existe un token
  status: authTokenStorage.get()
    ? "checking"
    : "unauthenticated",

  isAuthenticated: false,
  user: null,

  /**
   * Se ejecuta después del login.
   *
   * El token ya debe estar guardado en authTokenStorage.
   */
  setAuthenticated: (value) => {
    sessionVersion++;
    pendingCheck = null;

    clearAuthQueries();

    set({
      status: value ? "checking" : "unauthenticated",
      isAuthenticated: false,
      user: null,
    });
  },

  /**
   * Cierra la sesión.
   *
   * - Elimina el token.
   * - Limpia los datos privados de la caché.
   * - Restablece Zustand.
   */
  logout: () => {
    sessionVersion++;
    pendingCheck = null;

    authTokenStorage.clear();
    clearAuthQueries();

    set({
      status: "unauthenticated",
      isAuthenticated: false,
      user: null,
    });
  },

  /**
   * Comprueba la sesión mediante GET auth/user.
   *
   * Utiliza TanStack Query para compartir la caché
   * con useAuthUser() y ProfilePage.
   */
  checkSession: () => {
    const token = authTokenStorage.get();

    // Sin token no existe sesión
    if (!token) {
      get().logout();
      return Promise.resolve();
    }

    // Sesión ya verificada
    if (get().status === "authenticated") {
      return Promise.resolve();
    }

    // Reutilizar la petición en curso
    if (pendingCheck) {
      return pendingCheck;
    }

    const version = ++sessionVersion;

    set({
      status: "checking",
      isAuthenticated: false,
      user: null,
    });

    const request = (async () => {
      try {
        // Consulta compartida con TanStack Query
        const response = await queryClient.fetchQuery(
          authUserQuery()
        );

        // Ignorar respuestas de sesiones anteriores
        if (
          version !== sessionVersion ||
          authTokenStorage.get() !== token
        ) {
          return;
        }

        // Sesión validada correctamente
        set({
          status: "authenticated",
          isAuthenticated: true,
          user: response.data,
        });
      } catch (error) {
        // Ignorar errores de sesiones anteriores
        if (
          version !== sessionVersion ||
          authTokenStorage.get() !== token
        ) {
          return;
        }

        // Token rechazado por el backend
        if (
          error instanceof ApiError &&
          error.status === 401
        ) {
          get().logout();
          return;
        }

        // Error de conexión, timeout u otro error
        // No eliminamos el token automáticamente
        set({
          status: "error",
          isAuthenticated: false,
          user: null,
        });
      }
    })();

    pendingCheck = request;

    void request.finally(() => {
      if (pendingCheck === request) {
        pendingCheck = null;
      }
    });

    return request;
  },
}));
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="authStore.ts",
            content=content
        )
      


    def create_hooks_use_auth_user(self, full_path):
        """
        Genera el archivo.
        """
    
        folder_path = os.path.join(full_path, "src", "modules", "auth", "hooks")
    
        content = r'''// auth/hooks/useAuthUser.ts
import { useQuery } from "@tanstack/react-query";
import { authUserQuery } from "../queries/authUserQuery";

export const useAuthUser = () => {
  return useQuery(authUserQuery());
};
'''
    
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="useAuthUser.ts",
            content=content
        )


    def create_auth_user_query_ts(self, full_path):
        """
        Genera el archivo.
        """
    
        folder_path = os.path.join(full_path, "src", "modules", "auth", "queries")
    
        content = r'''// auth/queries/authUserQuery.ts
import { queryOptions } from "@tanstack/react-query";
import { getAuthUser } from "../services/authUserService";

export const authUserQuery = () =>
  queryOptions({
    queryKey: ["auth", "user"],
    queryFn: ({ signal }) => getAuthUser(signal),
    staleTime: 60 * 1000,
    retry: false,
});
'''
    
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="authUserQuery.ts",
            content=content
        )




    def create_auth_permissions_ts(self, full_path):
        """
        Genera el archivo.
        """
    
        folder_path = os.path.join(full_path, "src", "modules", "auth", "utils")
    
        content = r'''// src/modules/auth/utils/authPermissions.ts
import type { AuthUser } from "../types/auth-user.types";

/**
 * Roles disponibles en la aplicación.
 */
export type Role = "admin" | "manager" | "user";

/**
 * Obtiene los roles del usuario autenticado.
 */
export const getUserRoles = (user: AuthUser | null): string[] => {
  if (!user) return [];

  return (
    user.relationships?.roles?.map(
      (role) => role.attributes.name
    ) ?? []
  );
};

/**
 * Comprueba si el usuario tiene alguno de los roles indicados.
 *
 * Ejemplo:
 * hasRole(user, ["admin", "manager"])
 */
export const hasRole = (
  user: AuthUser | null,
  roles: Role[]
): boolean => {
  const userRoles = getUserRoles(user);

  return roles.some((role) => userRoles.includes(role));
};

/**
 * Comprueba si el usuario tiene todos los roles indicados.
 */
export const hasAllRoles = (
  user: AuthUser | null,
  roles: Role[]
): boolean => {
  const userRoles = getUserRoles(user);

  return roles.every((role) => userRoles.includes(role));
};

/**
 * Comprueba si el usuario es administrador.
 */
export const isAdmin = (user: AuthUser | null): boolean => {
  return hasRole(user, ["admin"]);
};
'''
    
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="authPermissions.ts",
            content=content
        )