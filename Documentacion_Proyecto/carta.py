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
        """Inicializa una carta con el palo y el número especificados.

        Args:
            palo (str): El palo de la carta.
            numero (int): El número de la carta.
        """
        self._palo = palo
        self._numero = numero

    @property
    def palo(self):
        """str: El palo de la carta."""
        return self._palo

    @palo.setter
    def palo(self, palo):
        """Establece el palo de la carta.

        Args:
            palo (str): El nuevo palo de la carta.
        """
        if palo in ["oros", "copas", "espadas", "bastos"]:
            self._palo = palo
        else:
            print("¡Ese no es un palo de la baraja!")

    @property
    def numero(self):
        """int: El número de la carta."""
        return self._numero

    @numero.setter
    def numero(self, numero):
        """Establece el número de la carta.

        Args:
            numero (int): El nuevo número de la carta.
        """
        if isinstance(numero, int):
            if numero in [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]:
                self._numero = numero
            else:
                print("El número de la carta debe estar entre 1 y 12")
                print("Excluyendo el 8 y el 9")
        else:
            print("El valor introducido debe ser númerico")

    def esta_en_mazo(self, mazo):
        """Comprueba si una determinada carta está en el mazo.

        Args:
            mazo (list): La lista de cartas en el mazo.

        Returns:
            bool: True si la carta está en el mazo, False en caso contrario.
        """
        for carta in mazo:
            if self.palo == carta.palo:
                if self.numero == carta.numero:
                    return True
        return False

    def __repr__(self):
        """Representación de la carta como una cadena."""
        return str(self.numero) + " de " + self._palo


class Mazo:
    """Clase Mazo.

    Representa un mazo de cartas, con métodos para crear un mazo
    completo, barajarlo y repartir cartas a jugadores.
    """

    def __init__(self):
        """Inicializa un nuevo mazo."""
        self._cartas = []
        self.rellenar()
        print(self._cartas)

    @property
    def cartas(self):
        """list: Las cartas en el mazo."""
        return self._cartas

    def rellenar(self):
        """Rellena el mazo con todas las cartas posibles y las baraja."""
        palos = ["oros", "copas", "espadas", "bastos"]
        numeros = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
        cartas = [Carta(p, n) for p in palos for n in numeros]
        shuffle(cartas)
        self._cartas = cartas

    def repartir(self, jugadores):
        """Reparte cartas a los jugadores especificados.

        Args:
            jugadores (list): Una lista de los nombres de los jugadores.
        """
        manos = {jugador: Mano(jugador) for jugador in jugadores}
        for _ in range(3):  # Repartir 3 cartas a cada jugador
            for jugador in jugadores:
                carta = self._cartas.pop()
                manos[jugador].recibir_carta(carta)
        for mano in manos.values():
            mano.mostrar_mano()


class Mano:
    """Clase Mano.

    Representa la mano de un jugador, con métodos para recibir cartas
    y mostrar la mano actual.
    """

    def __init__(self, jugador):
        """Inicializa una nueva mano para el jugador especificado.

        Args:
            jugador (str): El nombre del jugador.
        """
        self.jugador = jugador
        self.cartas = []

    def recibir_carta(self, carta):
        """Recibe una carta y la añade a la mano.

        Args:
            carta (Carta): La carta recibida.
        """
        self.cartas.append(carta)

    def mostrar_mano(self):
        """Muestra las cartas actuales en la mano del jugador."""
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
