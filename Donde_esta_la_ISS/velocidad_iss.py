import csv
from math import radians, sin, cos, sqrt, atan2

# Función para calcular la distancia entre dos puntos en la superficie de la Tierra
def calcular_distancia(lat1, lon1, lat2, lon2):
    # Radio de la Tierra en kilómetros
    radio_tierra = 6371.0

    # Convertir coordenadas de grados a radianes
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    # Diferencia de latitud y longitud
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Fórmula de Haversine
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Distancia entre los dos puntos
    distancia = radio_tierra * c

    return distancia

# Coordenadas y tiempo
with open('ejemplo.csv', 'r') as file:
    datos = csv.reader(file)
    coordenadas = []
    for dato in datos:
        dato_x, dato_y = dato
        # convertimos las cadenas en numeros
        dato_x = float(dato_x)
        dato_y = float(dato_y)
        coordenadas.append((dato_x,dato_y))
        
# coordenadas = [
#     (-40.2785, 56.2131),
#     (-40.4843, 56.5698),
#     # Inserta el resto de tus coordenadas aquí
# ]

tiempo_por_punto = 5  # segundos

# Calcular la velocidad promedio
distancias = []
for i in range(1, len(coordenadas)):
    lat1, lon1 = coordenadas[i - 1]
    lat2, lon2 = coordenadas[i]
    distancia = calcular_distancia(lat1, lon1, lat2, lon2)
    distancias.append(distancia)

# Calcular la velocidad promedio
velocidades = [distancia / tiempo_por_punto for distancia in distancias]
velocidad_promedio = sum(velocidades) / len(velocidades)

print("La velocidad promedio del satélite es:", velocidad_promedio, "km/s")
