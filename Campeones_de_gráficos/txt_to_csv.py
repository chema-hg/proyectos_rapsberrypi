"""txt_to_CSV.

Transforma el archivo medals.txt a un archivo csv.
"""

import re

# Abrir el archivo para lectura
with open('medals.txt', 'r') as file:
    # Leer todas las líneas del archivo
    lines = file.readlines()

# Abrir el archivo para escritura
with open('medals.csv', 'w') as file:
    # Iterar sobre cada línea del archivo original
    for line in lines:
        # Usar expresión regular para reemplazar espacios en blanco por comas
        cleaned_line = re.sub(r'\s(?![A-Z])', ',', line)
        # Eliminar el espacio en blanco después de la primera coma
        cleaned_line = re.sub(r',\s+', ',', cleaned_line)
        # Eliminar la coma final de la línea si existe
        cleaned_line = cleaned_line.rstrip(',')
        # Escribir la línea procesada en el archivo de salida y agregar un salto de línea
        file.write(cleaned_line + '\n')

