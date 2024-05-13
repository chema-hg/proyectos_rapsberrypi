import turtle as t

colores = {
    'rojomolon': '#df2707',
    'miazulete': '#7ebcc9',
    'fondo': '#A12BF5',
    'letrilla': '#E7F525',
    'fondocirculo': '#F5C625',
    'verderol': '#14E601',
    }

pantalla = t.Screen()
pantalla.setup(400, 400)
pantalla.bgcolor(colores['fondo'])
t.dot(300, colores['fondocirculo'])
t.penup()
t.right(90)
t.forward(180)
t.left(90)
t.pendown()
t.circle(180)

t.color(colores['rojomolon'])
estilo = ("Arial", 40, "bold")
t.write("HOLA", font = estilo, align = "center")
t.penup()
t.goto(0,100)
t.color(colores['letrilla'])
t.write("MUNDO", font = estilo, align = "center")
t.goto(0,0)
t.color(colores['verderol'])
t.write("Usando el módulo", font = ("Arial",25,"normal"), align = "center")
t.goto(0,-50)
t.write("TURTLE", font = estilo, align = "center")
t.hideturtle()




