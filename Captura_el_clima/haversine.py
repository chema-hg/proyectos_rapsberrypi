from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    #convierte ángulos de grados a radianes
    lon1 = radians(lon1)
    lat1 = radians(lat1)
    lon2 = radians(lon2)
    lat2 = radians(lat2)
    
    #formula de haversine
    dlon = lon2 - lon1
    dlat = lat2 - lat1    
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    distancia = 2 * asin(sqrt(a)) * 6371 
    #6371 es el radio de la tierra en km.
    return distancia

def dms_to_decimal(coord):
    # Verificar si la longitud de la coordenada es válida
    if len(coord) != 7:
        return None
    
    # Extraer los componentes de la coordenada
    grados = int(coord[:2])
    minutos = int(coord[2:4])
    segundos = int(coord[4:6])
    direccion = coord[-1]
    
    # Verificar la validez de la dirección
    if direccion not in ['N', 'S', 'E', 'W']:
        return None
    
    # Calcular la coordenada decimal
    decimal = grados + (minutos / 60) + (segundos / 3600) if direccion in ['N', 'E'] else -(grados + (minutos / 60) + (segundos / 3600))
    
    return decimal

# Ejemplo de uso
# lon = "012940W"
# lat = "405517N"
# lon = dms_to_decimal(lon)
# lat = dms_to_decimal(lat)
# distancia = haversine(-4.26946, 42.75948, lon, lat)
# print(distancia)
# print(decimal)
