import requests
from rich import print
from haversine import haversine, dms_to_decimal

# URLs de las estaciones y de los datos del clima
estaciones = "https://opendata.aemet.es/opendata/api/valores/climatologicos/inventarioestaciones/todasestaciones/"
clima = "https://opendata.aemet.es/opendata/api/observacion/convencional/datos/estacion/"

# API Key proporcionada por la AEMET
KEY = "Intruce la Key que te enviaron al email."

# Mis coordenadas
mi_lat = 42.75948
mi_lon = -4.26946

# Listado de todas las estaciones metereológicas.
querystring = {"api_key": KEY}
headers = {
    'cache-control': "no-cache"
    }
respuesta = requests.request("GET", estaciones, headers=headers, params=querystring)
datos_estaciones = respuesta.json()
lista_estaciones = requests.get(datos_estaciones['datos'])
estaciones = lista_estaciones.json()

def encontrar_cercana():
    menor_distancia = 20_036
    for estacion in estaciones:
        estacion_lon = estacion['longitud']
        estacion_lat = estacion['latitud']
        #convertimos grados dms a grados decimales
        estacion_lon = dms_to_decimal(estacion_lon)
        estacion_lat = dms_to_decimal(estacion_lat)
        distancia = haversine(mi_lon, mi_lat, estacion_lon, estacion_lat)
        # si la distancia es menor que la almacenada la guardamos
        if distancia < menor_distancia:
            menor_distancia = distancia
            estacion_mas_cercana = estacion['indicativo']
    return estacion_mas_cercana


idema = encontrar_cercana()
print(f"La estación mas cercana tiene el idema {idema}")
clima = clima + str(idema)
respuesta = requests.request("GET", clima, headers=headers, params=querystring)
datos_estacion = respuesta.json()
print(datos_estacion)
respuesta = requests.get(datos_estacion['datos'])
datos_clima = respuesta.json()
# La respuesta nos da los datos de las ultimas 24 horas
# Queremos imprimir solo la última observación.
print(datos_clima[-1])





