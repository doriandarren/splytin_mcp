# TODO Pendientes:


# Dorian tengo que terminar esto:

- Cambiar User en el generador IndexUser - Service en el "use" cuando se importa el user 
 



# Ejecutar nodulo:


```sh

python3 -m gen.php_laravel.to_module_crud.generate_model_file
python3 -m gen.php_laravel.to_module_crud.generate_postman_file

```

# Example 1:

```sh

[{'is_fk': True,
  'is_index': False,
  'is_nullable': False,
  'is_unique': False,
  'is_unsigned': False,
  'name': 'user_id',
  'options': ['fk'],
  'precision': None,
  'raw_type': 'fk',
  'related_model': 'User',
  'related_table': 'users',
  'relationship_column': 'user_id',
  'relationship_name': 'user',
  'scale': None,
  'size': None,
  'type': 'fk'},
 {'is_fk': False,
  'is_index': False,
  'is_nullable': False,
  'is_unique': True,
  'is_unsigned': False,
  'name': 'name',
  'options': ['string(30)', 'unique'],
  'precision': None,
  'raw_type': 'string(30)',
  'scale': None,
  'size': 30,
  'type': 'string'},
 {'is_fk': False,
  'is_index': False,
  'is_nullable': False,
  'is_unique': False,
  'is_unsigned': False,
  'name': 'amount',
  'options': ['decimal(10,2)'],
  'precision': 10,
  'raw_type': 'decimal(10,2)',
  'scale': 2,
  'size': None,
  'type': 'decimal'},
 {'is_fk': False,
  'is_index': False,
  'is_nullable': False,
  'is_unique': False,
  'is_unsigned': False,
  'name': 'amount_with_tax',
  'options': ['float'],
  'precision': None,
  'raw_type': 'float',
  'scale': None,
  'size': None,
  'type': 'float'},
 {'is_fk': False,
  'is_index': False,
  'is_nullable': False,
  'is_unique': False,
  'is_unsigned': False,
  'name': 'description',
  'options': ['varchar(10)'],
  'precision': None,
  'raw_type': 'varchar(10)',
  'scale': None,
  'size': 10,
  'type': 'string'},
 {'is_fk': False,
  'is_index': False,
  'is_nullable': False,
  'is_unique': False,
  'is_unsigned': False,
  'name': 'note',
  'options': ['string'],
  'precision': None,
  'raw_type': 'string',
  'scale': None,
  'size': 255,
  'type': 'string'},
 {'is_fk': False,
  'is_index': False,
  'is_nullable': False,
  'is_unique': False,
  'is_unsigned': False,
  'name': 'has_active',
  'options': ['boolean'],
  'precision': None,
  'raw_type': 'boolean',
  'scale': None,
  'size': None,
 }
]
```




# Example 2:

```sh

[{'is_fk': True,
  'is_index': False,
  'is_nullable': False,
  'is_unique': False,
  'is_unsigned': False,
  'name': 'user_id',
  'options': ['fk'],
  'precision': None,
  'raw_type': 'fk',
  'related_model': 'User',
  'related_table': 'users',
  'relationship_column': 'user_id',
  'relationship_name': 'user',
  'scale': None,
  'size': None,
  'type': 'fk'},
 {'is_fk': False,
  'is_index': False,
  'is_nullable': False,
  'is_unique': True,
  'is_unsigned': False,
  'name': 'name',
  'options': ['string(30)', 'unique'],
  'precision': None,
  'raw_type': 'string(30)',
  'scale': None,
  'size': 30,
  'type': 'string'},
 {'is_fk': False,
  'is_index': False,
  'is_nullable': False,
  'is_unique': False,
  'is_unsigned': False,
  'name': 'amount',
  'options': ['decimal(10,2)'],
  'precision': 10,
  'raw_type': 'decimal(10,2)',
  'scale': 2,
  'size': None,
  'type': 'decimal'},
 {'is_fk': False,
  'is_index': False,
  'is_nullable': False,
  'is_unique': False,
  'is_unsigned': False,
  'name': 'amount_with_tax',
  'options': ['float'],
  'precision': None,
  'raw_type': 'float',
  'scale': None,
  'size': None,
  'type': 'float'},
 {'is_fk': False,
  'is_index': False,
  'is_nullable': False,
  'is_unique': False,
  'is_unsigned': False,
  'name': 'description',
  'options': ['varchar(10)'],
  'precision': None,
  'raw_type': 'varchar(10)',
  'scale': None,
  'size': 10,
  'type': 'string'},
 {'is_fk': False,
  'is_index': False,
  'is_nullable': False,
  'is_unique': False,
  'is_unsigned': False,
  'name': 'note',
  'options': ['string'],
  'precision': None,
  'raw_type': 'string',
  'scale': None,
  'size': 255,
  'type': 'string'},
 {'is_fk': False,
  'is_index': False,
  'is_nullable': False,
  'is_unique': False,
  'is_unsigned': False,
  'name': 'has_active',
  'options': ['boolean'],
  'precision': None,
  'raw_type': 'boolean',
  'scale': None,
  'size': None,
 }
]

```









# Blender ---> Dariana haciendo:

```sh

barriles de maderas
barriles de aceros (gasolina)


Lista de objetos:

cajas de madera
cajas rotas
mesas
sillas
bancos
estanterías
armarios
puertas viejas apoyadas

faroles
velas
botellas
libros
platos
jarras
sacos
cubos

árboles
troncos cortados
rocas
vallas de madera
postes
señales

lámparas
faroles colgantes
antorchas
interruptores (opcional)
cables

```



# Pendiete con Kotlin

```sh

- hacer strings.xml

- Edita gradle/libs.versions.toml:

[versions]
navigationCompose = "2.9.7"

[libraries]
androidx-navigation-compose = { group = "androidx.navigation", name = "navigation-compose", version.ref = "navigationCompose" }
androidx-compose-material-icons-extended = { group = "androidx.compose.material", name = "material-icons-extended" }
androidx-compose-material = { group = "androidx.compose.material", name = "material" }



- Edita: app/build.gradle.kts:

dependencies:
implementation(libs.androidx.navigation.compose)
implementation(libs.androidx.compose.material)
implementation("com.squareup.retrofit2:retrofit:2.11.0")
implementation("com.squareup.retrofit2:converter-gson:2.11.0")



- Editar el AndroidManifest.xml:

<uses-permission android:name="android.permission.INTERNET" />





- Modificar MainActivity.kt
- Agregar AppNavigation.kt




- crear Core:

com.www.testgeneratorandroid.core.network
-> RetrofitClient.kt


- Modulo Auth:

com.www.testgeneratorandroid.modules.auth.models
-> LoginRequest.kt
-> LoginResponse.kt
-> AuthResponse.kt

com.www.testgeneratorandroid.modules.auth.repositories
-> AuthRepository.kt

com.www.testgeneratorandroid.modules.auth.screens
-> LoginScreen.kt

com.www.testgeneratorandroid.modules.auth.services
-> AuthApiService.kt







com.www.testgeneratorandroid.ui.screens -> Agregar HomeScreen.kt y Agregar LoginScreen.kt


com.www.testgeneratorandroid.data.models
com.www.testgeneratorandroid.data.network
com.www.testgeneratorandroid.data.repositories




```





## Prompt Python Django API

```sh

Para que entiendas el conexto que necesito. Tengo una carpeta en la raíz del proyecto por ejemplo: apps/AiTextGenerationPrompt/api. Con estas carpetas: router.py, serializers.py y views.py

router.py:

from rest_framework.routers import DefaultRouter
from apps.users.api.views import UserApiViewSet

router = DefaultRouter()

router.register(
    prefix='users',
    basename='users',
    viewset=UserApiViewSet
)

urlpatterns = router.urls


serializers.py:

from rest_framework.serializers import ModelSerializer
from apps.users.models import User

class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'is_staff',
        ]


views.py:

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.users.api.serializers import UserSerializer
from apps.users.models import User

class UserApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UserSerializer
    queryset = User.objects.all()

```






# Pendiente con UE5:

- Crear carpeta Maps




# TODO astro:

- Crear proyecto:
npm create astro@latest
npm create astro@latest -- --template basics


- Modificar iconos

- Tailwind:
npx astro add tailwind

## en sytles/globals.css agregar:

@theme {
    ...
}


## luego agregar en el Layout: 
---
import "../styles/global.css";
---


- Animate css: 
npm install animate.css

y en el Layout.astro: 
...
import "animate.css";
import "../styles/global.css";
...



- Activar React y Mapa leaflet

npx astro add react         # Activa React para Astro

npm install leaflet

## Copiar de otros proyecto en el componente donde vaya estar 



- SiteMap

npx astro add sitemap

## y luego en astro.config.mjs el nombre del sitio:

export default defineConfig({
    site: 'https://template.splytin.com',
    ...
...



- Cookies:

npx astro add @jop-software/astro-cookieconsent

## Modificar el astro.config.mjs








# Project

```sh



```