"""¿Donde está la Estación Espacial Internacional?.

Muestra la ISS en un momento en concreto.
"""

import urllib.request
import json
import turtle

# http://open-notify.org/Open-Notify-API/
URL = 'http://api.open-notify.org/astros.json'
with urllib.request.urlopen(URL) as respuesta:
    astronautas = json.loads(respuesta.read())

print(f"Número actual de astronautas: {astronautas['number']}")
for persona in astronautas['people']:
    print(f"{persona['name']} está en {persona['craft']}")

URL = 'http://api.open-notify.org/iss-now.json'
with urllib.request.urlopen(URL) as respuesta:
    iss_posicion = json.loads(respuesta.read())

coordenadas = iss_posicion['iss_position']
lat = float(coordenadas['latitude'])
long = float(coordenadas['longitude'])
print(f"Latitud: {lat}, Longitud: {long}")

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
iss.goto(long, lat)

num_personas = turtle.Turtle()
num_personas.penup()
num_personas.hideturtle()
# color del texto
num_personas.color('yellow')
# Ir al punto en el mapa
num_personas.goto(-175, -25)
num_personas.write(f"Nº Astronautas: {astronautas['number']}")
