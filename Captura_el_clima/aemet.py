import requests
from rich import print

url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/inventarioestaciones/todasestaciones/"

# API Key proporcionada por la AEMET
KEY = "usa la key que te han enviado al email."

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
respuesta = requests.get(URL)
print(respuesta)
datos = respuesta.json()
print(datos)

# for dato in datos:
#     #if dato['provincia'] == 'LEON':
#     print(dato)


#print(response.text)
