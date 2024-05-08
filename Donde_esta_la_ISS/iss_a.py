"""¿Donde está la Estación Espacial Internacional?.

Muetra la ISS en movimiento hasta que se cierre el programa.
"""

import requests
import turtle
import time

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

while True:
    URL = 'http://api.open-notify.org/iss-now.json'
    with requests.get(URL) as respuesta:
        iss_posicion = respuesta.json()
    coordenadas = iss_posicion['iss_position']
    lat = float(coordenadas['latitude'])
    long = float(coordenadas['longitude'])
    print(f"Latitud: {lat}, Longitud: {long}")    
    iss.goto(long, lat)
    iss.pendown()
    time.sleep(5)
    
    
    
    
    
