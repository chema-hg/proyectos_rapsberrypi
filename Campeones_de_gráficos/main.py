"""Campeones de gráficos.

Utilización de la librería Pygal para crear
gráficos.
"""

import webbrowser
from pygal import Bar


# Creando un gráfico
# Importa y usa Pie si se quiere un gráfico circular.
grafico = Bar(title="Medallas Olímpicas")

# Añadiendo datos
us = ['Estados Unidos', 2655]
gb = ['Gran Bretaña', 931]
ch = ['China', 634]
al = ['Alemania', 797]
fr = ['Francia', 772]
sp = ['España', 169]

# grafico.add(us[0], us[1])
# grafico.add(gb[0], gb[1])
# grafico.add(fr[0], fr[1])
# grafico.add(sp[0], sp[1])
# grafico.add(ch[0], ch[1])
# grafico.add(al[0], al[1])

with open('medals.csv', 'r') as lineas:
    for linea in lineas:
        linea = linea.strip()
        dato = linea.split(',')
        grafico.add(dato[0], int(dato[5]))

grafico.render_to_file('prueba.svg')
webbrowser.open('prueba.svg')

# Para abrirlo directamente en el programa por defecto del sistema
# en mi caso el visor de imagenes.
# import subprocess
# subprocess.run(["xdg-open","prueba.svg"])
