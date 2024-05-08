"""Mazo de Cartas.

Programa para mostrar el funcionamiento de las clases
a través de una baraja.
"""
# from pprint import pprint as print
from random import shuffle


class Carta:
    """Clase Carta.

    La clase carta representa una única carta y se
    inicializa pasandole el palo y número de la carta a
    representar.
    """

    def __init__(self, palo, numero):
        self._palo = palo
        self._numero = numero

    # getter y setter para el atriburo palo
    @property
    def palo(self):
        return self._palo

    @palo.setter
    def palo(self, palo):
        if palo in ["oros", "copas", "espadas", "bastos"]:
            self._palo = palo
        else:
            print("¡Ese no es un palo de la baraja!")

    # getter y setter para el atriburo numero
    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        if isinstance(numero, int):
            if numero in [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]:
                self._numero = numero
            else:
                print("El número de la carta debe estar entre 1 y 12")
                print("Excluyendo el 8 y el 9")
        else:
            print("El valor introducido debe ser númerico")

    def esta_en_mazo(self, mazo):
        """Comprueba si una determinada carta esta en el mazo que le
        pasamos o no"""
        for carta in mazo:
            if self.palo == carta.palo:
                if self.numero == carta.numero:
                    return True
        return False

    def __repr__(self):
        return str(self.numero) + " de " + self._palo


class Mazo:
    def __init__(self):
        self._cartas = []
        self.rellenar()
        print(self._cartas)

    # Creamos un getter
    @property
    def cartas(self):
        return self._cartas

    def rellenar(self):
        palos = ["oros", "copas", "espadas", "bastos"]
        numeros = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
#         cartas = [] # Crea una lista vacia de cartas
#         for palo in palos: # Por cada palo
#             for numero in numeros: # Por cada numero
#                 # Creamos un nuevo objeto Carta y lo añadimos a la lista.
#                 cartas.append(Carta(palo, numero))
#         self._cartas = cartas # Apuntamos a esta lista con self._cartas
#         self._cartas = [ Carta(p, n) for p in palos for n in numeros ]
        # Devuelve un mazo con las cartas en orden aleatorio.
        cartas = [Carta(p, n) for p in palos for n in numeros]
        shuffle(cartas)
        self._cartas = cartas

    def repartir(self, jugadores):
        manos = {jugador: Mano(jugador) for jugador in jugadores}
        for _ in range(3):  # Repartir 3 cartas a cada jugador
            for jugador in jugadores:
                carta = self._cartas.pop()
                manos[jugador].recibir_carta(carta)
        for mano in manos.values():
            mano.mostrar_mano()


class Mano:
    def __init__(self, jugador):
        self.jugador = jugador
        self.cartas = []

    def recibir_carta(self, carta):
        self.cartas.append(carta)

    def mostrar_mano(self):
        print(f"Mano de {self.jugador}:")
        for carta in self.cartas:
            print(carta)


mi_mazo = Mazo()
mi_carta = Carta("dragon", 5)
print(mi_carta.esta_en_mazo(mi_mazo.cartas))
# jugador_1 = mi_mazo.repartir()
# jugador_2 = mi_mazo.repartir()
jugadores = ["Jugador 1", "Jugador 2"]
mi_mazo.repartir(jugadores)
