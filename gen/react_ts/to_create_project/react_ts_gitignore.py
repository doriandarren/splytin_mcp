import os
from gen.helpers.helper_file import HelperFile


class ReactTsGitignore:

    def invoke(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path)

        content = r'''# ============================================
# React + TypeScript + Vite
# ============================================

# Dependencias
node_modules/
.pnp.*
.yarn/cache/
.yarn/unplugged/
.yarn/build-state.yml
.yarn/install-state.gz

# Compilación
dist/
dist-ssr/
build/
*.local

# Caché
.cache/
.vite/
node_modules/.vite/
*.tsbuildinfo
.eslintcache

# Logs
logs/
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*

# Variables de entorno y secretos
.env
.env.*
!.env.example
!.env.sample

# Archivos temporales
tmp/
temp/
*.tmp
*.temp
*.swp
*.swo
*~

# Testing y cobertura
coverage/
.nyc_output/
playwright-report/
test-results/

# IDE - VS Code
.vscode/*
!.vscode/extensions.json
!.vscode/settings.json
!.vscode/launch.json

# IDE - JetBrains
.idea/
*.iml

# Sistema operativo - macOS
.DS_Store
.AppleDouble
.LSOverride
._*

# Sistema operativo - Windows
Thumbs.db
Thumbs.db:encryptable
Desktop.ini
$RECYCLE.BIN/

# Sistema operativo - Linux
.directory
.Trash-*

# TypeScript
*.tsbuildinfo

# Archivos de respaldo
*.bak
*.backup
*.old

# Certificados y claves privadas
*.pem
*.key
*.p12
*.pfx
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name=".gitignore",
            content=content
        )