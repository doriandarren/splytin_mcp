import os
from gen.helpers.helper_columns import HelperColumns
from gen.helpers.helper_file import HelperFile
from gen.react_ts.to_create_module_crud.standard_module_crud_react_ts import StandardModuleCrudReactTs


class ReactTsProfile:
    
    def invoke(self, full_path):
        self.create_module(full_path)
        self.update_file_profie(full_path)



    def create_module(self, full_path):
        columns = HelperColumns.parse_columns_input("name email roles")

        obj = StandardModuleCrudReactTs()
        obj.invoke(
            full_path=full_path,
            namespace="private",
            singular_name="Profile",
            plural_name="Profiles",
            columns=columns,
            input_menu_checkbox=None,
            version_api="V1",
            folder_group="api"
        )



    def update_file_profie(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "src", "modules", "private", "profiles", "pages")

        content = r'''
import { RefreshCw, UserRound, Mail, ShieldCheck } from "lucide-react";

import { Button } from "@/components/ui/button";
import { useAuthUser } from "@/modules/auth/hooks/useAuthUser";

export const ProfilePage = () => {
  const {
    data,
    isPending,
    isError,
    isFetching,
    refetch,
  } = useAuthUser();

  if (isPending) {
    return (
      <div className="p-6">
        <p className="text-muted-foreground">
          Cargando perfil...
        </p>
      </div>
    );
  }

  if (isError) {
    return (
      <div className="space-y-4 p-6">
        <p className="text-destructive">
          No se pudo cargar el perfil.
        </p>

        <Button onClick={() => void refetch()}>
          Reintentar
        </Button>
      </div>
    );
  }

  const user = data.data;

  return (
    <div className="mx-auto max-w-3xl space-y-6 p-6">
      <div>
        <h1 className="text-3xl font-bold">
          Mi perfil
        </h1>

        <p className="mt-2 text-muted-foreground">
          Información de tu cuenta.
        </p>
      </div>

      <div className="space-y-6 rounded-xl border bg-card p-6">
        <div className="flex items-center gap-3">
          <div className="rounded-full bg-muted p-3">
            <UserRound className="size-6" />
          </div>

          <div>
            <h2 className="text-xl font-semibold">
              {user.attributes.name}
            </h2>

            <p className="text-sm text-muted-foreground">
              Usuario #{user.id}
            </p>
          </div>
        </div>

        <div className="grid gap-6 sm:grid-cols-2">
          <div className="space-y-2">
            <div className="flex items-center gap-2 text-sm text-muted-foreground">
              <Mail className="size-4" />
              Correo electrónico
            </div>

            <p className="font-medium">
              {user.attributes.email}
            </p>
          </div>

          <div className="space-y-2">
            <div className="flex items-center gap-2 text-sm text-muted-foreground">
              <ShieldCheck className="size-4" />
              Roles
            </div>

            <p className="font-medium">
              {user.relationships?.roles
                ?.map((role) => role.attributes.name)
                .join(", ") || "Sin roles"}
            </p>
          </div>
        </div>

        <div className="flex justify-end border-t pt-4">
          <Button
            variant="outline"
            onClick={() => void refetch()}
            disabled={isFetching}
          >
            <RefreshCw
              className={
                isFetching ? "size-4 animate-spin" : "size-4"
              }
            />
            Actualizar perfil
          </Button>
        </div>
      </div>
    </div>
  );
};        
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="ProfilePage.tsx",
            content=content
        )

