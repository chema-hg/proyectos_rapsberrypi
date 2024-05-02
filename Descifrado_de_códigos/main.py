"""Descifrador de códigos.

Codifica o decodifica un texto usando el cifrado atbash
y permite realizar un ánalisis de frecuencias."""

from pygal import Bar

# Crear el código Atbash invirtiendo el alfabeto


def crear_codigo():
    """Crea el código que utilizaremos para codificar
    o decodificar el mensaje. Será un diccionario."""
    # reversa del ALFABETO
    inversa = list(reversed(ALFABETO))

    for i in range(len(ALFABETO)):  # Longitud de una lista
        codigo[ALFABETO[i]] = inversa[i]
        # Rellena el alfabeto con una letra y su correspondiente
        # letra códificada.

    # Lista de caracteres especiales y sus equivalentes en el alfabeto normal
    caracteres_especiales = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}

    # Agregar caracteres especiales al diccionario de códigos
#     for especial, normal in caracteres_especiales.items():
#         codigo[especial] = codigo[normal]
    codigo.update(caracteres_especiales)

    # print(codigo)


def atbash(texto):
    """Codifica o decodifica una línea de texto.
    Atbash es símetrico.
    """
    texto = texto.lower()  # Convierte el texto en minúsculas.
    salida = ""

    for letra in texto:
        if letra in codigo:
            salida += codigo[letra]

    return salida


def menu():
    """Crea un menú basado en texto."""
    eleccion = ""

    while eleccion != 'c' and eleccion != 'f':
        eleccion = input('''Por favor, introduce c para codificar/decodificar texto,
o f para realizar un análisis de frecuencias: \n''')

        if eleccion == 'c':
            print("Pasando tu mensaje a través del cifrado...")
            # mensaje = "Mi mensaje secreto"
            mensaje = obtener_texto('datos.txt')
            codigo = atbash(mensaje)
            print(codigo)

        elif eleccion == 'f':
            mensaje = obtener_texto('datos.txt')
            codigo = atbash(mensaje)
            mensaje_frec = frecuencia(codigo)
            print(mensaje_frec)
            lang_freq = spanish  # Importamos la frecuencia de la letras en español
            # llama a la función que crea el gráfico
            crear_grafico(mensaje_frec, lang_freq)


def obtener_texto(nombre_archivo):
    """Obtiene y devuelve texto desde un archivo."""
    with open(nombre_archivo) as f:
        # tenemos que eliminar los saltos de linea.
        texto = f.read().replace('\n', " ")
        return texto


def frecuencia(texto):
    """Calcula la frecuencia de las letras en un texto"""
    texto = list(texto.lower())

    frec = {}

    for letra in texto:
        if letra != " ":
            frec[letra] = frec.get(letra, 0) + 1

    # número total de letras sin espacions en blanco
    letras_totales = sum(frec.values())

    for letra in frec:
        # Convierte números en porcentajes.
        frec[letra] = frec[letra] / letras_totales * 100

    return frec


def crear_grafico(texto, lenguaje):
    """Crea el gráfico de frecuencias"""
    grafico = Bar(width=800, height=400, title="Análisis de Frecuencias",
                  x_labels=list(lenguaje.keys()))
    # Etiquetas de las frecuencias para el mensaje codificado.
    valores = []
    for i in lenguaje:
        valores.append(texto.get(i, 0))
    grafico.add('Mensaje objetivo', valores)
    # Etiquetas de las frecuencias de las letras en el idioma español
    grafico.add('Lenguaje', list(lenguaje.values()))

    grafico.render_to_file('grafico.svg')


# Estructura de datos
# Lista creada desde una cadena de texto
ALFABETO = list(" abcdefghijklmnñopqrstuvwxyz ")
codigo = {}
spanish = {'a': 12.53, 'b': 1.42, 'c': 4.68, 'd': 5.86, 'e': 13.68, 'f': 0.69, 'g': 1.01, 'h': 0.70,
           'i': 6.25, 'j': 0.44, 'k': 0.02, 'l': 4.97, 'm': 3.15, 'n': 6.71, 'ñ': 0.31, 'o': 8.68,
           'p': 2.51, 'q': 0.88, 'r': 6.97, 's': 7.98, 't': 4.63, 'u': 3.93, 'v': 0.90, 'w': 0.01,
           'x': 0.22, 'y': 0.90, 'z': 0.52}

# Comienzo


def main():
    crear_codigo()
    # print(atbash("Codificar es fácil"))
    menu()


main()
