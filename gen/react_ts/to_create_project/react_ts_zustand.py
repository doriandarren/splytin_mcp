import os
from gen.helpers.helper_file import HelperFile
from gen.helpers.helper_print import print_green, run_command


class ReactTsZustand:


    def invoke(self, full_path):
        self.install(full_path)
        self.create_auth_store_ts(full_path)
        self.create_protected_route_tsx(full_path)
    
    
    
    
    def install(self, full_path):
        # Instalar dependencias
        run_command(
            "npm install zustand",
            cwd=full_path
        )
        
        print_green("zustand creado correctamente.")
    
    
    
    def create_auth_store_ts(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "src", "modules", "auth", "stores")

        content = r'''import { create } from "zustand";
import { authTokenStorage } from "../services/authTokenStorage";

interface AuthState {
  isAuthenticated: boolean;
  setAuthenticated: (value: boolean) => void;
  logout: () => void;
}

export const useAuthStore = create<AuthState>((set) => ({
  isAuthenticated: Boolean(authTokenStorage.get()),

  setAuthenticated: (value) => {
    set({ isAuthenticated: value });
  },

  logout: () => {
    authTokenStorage.clear();
    set({ isAuthenticated: false });
  },
}));

'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="authStore.ts",
            content=content
        )
        
        
    
    def create_protected_route_tsx(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "src", "modules", "auth", "components")

        content = r'''import { Navigate, Outlet, useLocation } from "react-router";
import { useAuthStore } from "../stores/authStore";

export const ProtectedRoute = () => {
  const isAuthenticated = useAuthStore(
    (state) => state.isAuthenticated
  );

  const location = useLocation();

  if (!isAuthenticated) {
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