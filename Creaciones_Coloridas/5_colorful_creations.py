from turtle import *
'''uso de la tortuga y de colores hexadecimales en vez de nombres de color a traves de un diccionario'''

pantalla = Screen() #creamos el objeto pantalla de la clase Screen
pantalla.setup(700,400) #establecemos el area de la pantalla con el metodo setup
pantalla.bgcolor('#161361') #establecemos el fondo de la pantalla con el metodo bgcolor

colores ={
    'rojito':'#C92C0D',
    'amarillin':'#EFEF0A',
    'verderol':'#45EF0A',
    'azulete':'#2EACB4',
    'moradito':'B42EA8',   
    }

# https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Colors/Color_picker_tool
# pagina para escoger colores rgb, hexadecinales etc

goto(0,-200)
circle(200) # circle como su nombre indica dibuja un circulo.
goto(0,0)
color(colores['amarillin'])
dot(100) # el color de comienzo por defecto es negro.

penup() #para que no deje rastro al moverse
goto(0,100)
color(colores['verderol'])
style = ('Times', 50, 'bold')
write('HOLA', font=style, align='center')

right(90) # por defecto sale el puntero sale en el 0,0 y mirando a la derecha -->
forward(60)
color(colores['amarillin']) #vuelvo a cambiar el color del puntero que antes era verderol
write('Me voy a hacer footing', font=style, align='center')

hideturtle() #para que no se vea el puntero