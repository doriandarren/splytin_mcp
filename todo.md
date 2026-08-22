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


[tows] Tow *** Tows : transporeon_plate:varchar(255) msoft_plate:varchar(255)


[daily_summaries] DailySummary *** DailySummaries : start_date:timestamp end_date:timestamp total_created_transport:int(11) total_updated_transport:int(11) total_deleted_transport:int(11) avg_created_transport_15_days:double(10,2) avg_created_transport_30_days:double(10,2) avg_created_transport_3_months:double(10,2)


[transporeon_shipment_stations] TransporeonShipmentStation *** TransporeonShipmentStations : transporeon_shipment_id:fk station_identifier:varchar(255) type:varchar(255) company_name:varchar(255) address:varchar(255) zip:varchar(255) region:varchar(255) city:varchar(255) country:varchar(255) from_date:varchar(255) from_time:varchar(255) from_at:timestamp

[items] Item *** Items : description:varchar(255) transporeon_item_id:varchar(255) msoft_item_id:varchar(255)

[transporeon_shipment_items] TransporeonShipmentItem *** TransporeonShipmentItems : transporeon_shipment_id:fk item_identifier:varchar(255) description:varchar(255) pos_number:varchar(255) pos_index:varchar(255) material_number:varchar(255)

[transports] Transport *** Transports : provider_id:fk transport_identifier:varchar(255) number:varchar(255) changed:text status:text qualifier:varchar(255) document_reference:text vehicle_name:varchar(255) service_id:fk start_date:varchar(255) start_time:varchar(255) start_at:timestamp comment:text plate:varchar(255) transporeon_sent_at:timestamp transporeon_response_json:longtext is_transporeon_updated:tinyint(1) transporeon_updated_nb:int(11) msoft_numero_expedicion:varchar(255) msoft_modo:varchar(20) msoft_empresa_contexto:varchar(20) msoft_centro_contexto:varchar(20) msoft_session_contexto:varchar(20) msoft_sent_at:timestamp msoft_request_json:text msoft_response_result:varchar(255) msoft_response_code:varchar(255) msoft_response_description:varchar(255) msoft_response_json:text msoft_response_key:varchar(255)



[transporeon_transports] TransporeonTransport *** TransporeonTransports : transport_identifier:varchar(255) number:varchar(255) changed:text status:text qualifier:varchar(255) document_reference:text vehicle_name:varchar(255) start_date:varchar(255) start_time:varchar(255) start_at:timestamp comment:text is_processed:varchar(255) is_selected:tinyint(1)

[transporeon_shipments] TransporeonShipment *** TransporeonShipments : transporeon_transport_id:fk shipment_identifier:varchar(255) number:varchar(255) comment:text

[shipment_stations] ShipmentStation *** ShipmentStations : shipment_id:fk station_identifier:varchar(255) type:varchar(255) company_name:varchar(255) address:varchar(255) zip:varchar(255) region:varchar(255) city:varchar(255) country:varchar(255) from_date:varchar(255) from_time:varchar(255) from_at:timestamp

[agenda_unloadings] AgendaUnloading *** AgendaUnloadings : transporeon_code:varchar(255) name:varchar(255) msoft_code:varchar(255)

[msoft_settings] MsoftSetting *** MsoftSettings : token:text

[shipments] Shipment *** Shipments : provider_id:fk transport_id:fk shipment_identifier:varchar(255) number:varchar(255) comment:text

[transport_logs] TransportLog *** TransportLogs : transport_id:fk method_type:varchar(255) request:text

[providers] Provider *** Providers : name:varchar(255)

[shipment_items] ShipmentItem *** ShipmentItems : shipment_id:fk item_id:fk item_identifier:varchar(255) description:varchar(255)

[agenda_uploads] AgendaUpload *** AgendaUploads : transporeon_code:varchar(255) name:varchar(255) msoft_code:varchar(255)

[user_statuses] UserStatus *** UserStatuses : name:varchar(255)

[services] Service *** Services : description:varchar(255) service_code:varchar(255)


```