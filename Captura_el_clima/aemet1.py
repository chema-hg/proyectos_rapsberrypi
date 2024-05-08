import requests
from rich import print

url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/inventarioestaciones/todasestaciones/"

# API Key proporcionada por la AEMET
KEY = "Usa el api key enviada por la AEMET a tu correo."

querystring = {"api_key": KEY}

headers = {
    'cache-control': "no-cache"
    }

respuesta = requests.request("GET", url, headers=headers, params=querystring)

print(respuesta)

diccionario = respuesta.json()

print(diccionario)

URL = diccionario['datos']
print(URL)
respuesta = requests.get(URL)
estaciones = respuesta.json()

# Número de estaciones metereológicas
print(f'Hay {len(estaciones)} estaciones meteorológicas registradas en la AEMET')

print(estaciones[0])

URL = "https://opendata.aemet.es/opendata/api/observacion/convencional/datos/estacion/B013X"
respuesta = requests.request("GET", URL, headers=headers, params=querystring)
print(respuesta)
datos = respuesta.json()
print(datos)

URL = datos['datos']
respuesta = requests.get(URL)
datos_clima = respuesta.json()
print(datos_clima)


