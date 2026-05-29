# TODO Pendientes:


# Dorian tengo que terminar esto:

- En php: revisar boostrap/app.php que hay cosas nuevas






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

