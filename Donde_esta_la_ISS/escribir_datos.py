"""¿Donde está la Estación Espacial Internacional?."""

import requests
import turtle
import time
import csv

# http://open-notify.org/Open-Notify-API/
URL = 'http://api.open-notify.org/astros.json'
with requests.get(URL) as respuesta:
    print(respuesta)
    print(respuesta.text) # en formato json
    astronautas = respuesta.json() # en formato diccionario
    print(astronautas)

print(f"Número actual de astronautas: {astronautas['number']}")
for persona in astronautas['people']:
    print(f"{persona['name']} está en {persona['craft']}")
    
# map.jpg: https://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.gif')

screen.register_shape('station.gif')
iss = turtle.Turtle()
iss.shape('station.gif')
# iss.setheading(90) La tortuga mira a la derecha por defecto
iss.penup()
screen.colormode(255)
iss.pencolor(255,255,0)

# contador para guardar la long y latitud
contador = 0

while True:
    contador += 1
    URL = 'http://api.open-notify.org/iss-now.json'
    with requests.get(URL) as respuesta:
        iss_posicion = respuesta.json()
    coordenadas = iss_posicion['iss_position']
    lat = float(coordenadas['latitude'])
    long = float(coordenadas['longitude'])
    print(f"Latitud: {lat}, Longitud: {long}")    
    iss.goto(long, lat)
    iss.pendown()
    # Escribimos los datos en un archivo csv
    with open('ejemplo.csv', 'a') as file:
        datos_a_escribir = csv.writer(file)
        datos_a_escribir.writerow([lat, long])
    time.sleep(5)
    # La ISS tarda aproximandamente 91 minutos en dar
    # una vuelta a la tiera. 91*12 = 1092
    if contador == 1092:
        break