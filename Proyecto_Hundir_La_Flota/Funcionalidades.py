import random

import numpy as np


def crear_tablero(tamano=10):
    """Crea un tablero de tamaño tamano x tamano relleno con '_'"""
    return np.full((tamano, tamano), "_", dtype="U1")


def colocar_barco(barco, tablero):
    """Coloca un barco, representado por una lista de casillas, en el tablero."""
    for fila, columna in barco:
        if not (0 <= fila < tablero.shape[0] and 0 <= columna < tablero.shape[1]):
            raise ValueError("El barco se sale del tablero.")
        if tablero[fila, columna] != "_":
            raise ValueError("No puedes superponer barcos.")
        tablero[fila, columna] = "O"
    return tablero


def disparar(casilla, tablero):
    """Recibe una casilla (fila, columna) y actualiza el tablero."""
    fila, columna = casilla

    if not (0 <= fila < tablero.shape[0] and 0 <= columna < tablero.shape[1]):
        raise ValueError("La casilla está fuera del tablero.")

    if tablero[fila, columna] == "O":
        tablero[fila, columna] = "X"
        return True
    if tablero[fila, columna] == "_":
        tablero[fila, columna] = "A"
        return False

    return None


def crear_barco(eslora, tablero):
    """Genera una lista de casillas válidas para un barco aleatorio."""
    alto, ancho = tablero.shape

    for _ in range(1000):
        orientacion = random.choice(["horizontal", "vertical"])

        if orientacion == "horizontal":
            fila = random.randint(0, alto - 1)
            columna_inicial = random.randint(0, ancho - eslora)
            posiciones = [(fila, columna_inicial + i) for i in range(eslora)]
        else:
            fila_inicial = random.randint(0, alto - eslora)
            columna = random.randint(0, ancho - 1)
            posiciones = [(fila_inicial + i, columna) for i in range(eslora)]

        if all(
            0 <= fila < alto and 0 <= columna < ancho and tablero[fila, columna] == "_"
            for fila, columna in posiciones
        ):
            return posiciones

    raise ValueError(f"No se pudo crear un barco de eslora {eslora}.")


def colocar_barcos(tablero, configuracion=None):
    """Coloca una flota aleatoria siguiendo una configuración de tamaños."""
    if configuracion is None:
        configuracion = [2, 2, 2, 3, 3, 4]

    barcos = []

    for eslora in configuracion:
        while True:
            try:
                posiciones = crear_barco(eslora, tablero)
                for fila, columna in posiciones:
                    tablero[fila, columna] = "O"
                barcos.append(posiciones)
                break
            except ValueError:
                continue

    return barcos


def mostrar_tablero(tablero, ocultar_barcos=False):
    """Muestra el estado del tablero. Si ocultar_barcos=True, no enseña los barcos."""
    tablero_mostrar = tablero.copy()

    if ocultar_barcos:
        tablero_mostrar = np.where(tablero_mostrar == "O", "_", tablero_mostrar)

    print("   " + " ".join(str(i) for i in range(tablero.shape[1])))
    for fila_index, fila in enumerate(tablero_mostrar):
        print(str(fila_index) + "  " + " ".join(fila))


def casillas_disponibles(tablero):
    """Devuelve todas las casillas que no han sido disparadas todavía."""
    disponibles = []
    for fila in range(tablero.shape[0]):
        for columna in range(tablero.shape[1]):
            if tablero[fila, columna] not in {"A", "X"}:
                disponibles.append((fila, columna))
    return disponibles


def juego_vs_maquina():
    """Flujo principal del juego: jugador contra la máquina."""
    tablero_jugador = crear_tablero()
    tablero_maquina = crear_tablero()

    colocar_barcos(tablero_jugador)
    colocar_barcos(tablero_maquina)

    disparos_jugador = set()
    disparos_maquina = set()

    print("Bienvenido a Hundir la flota.")
    print("Tu tablero es el siguiente: ")
    mostrar_tablero(tablero_jugador)

    while True:
        print("\nTu turno:")
        while True:
            try:
                fila = int(input("Introduce la fila: "))
                columna = int(input("Introduce la columna: "))
                casilla = (fila, columna)
                if casilla in disparos_jugador:
                    print("Ya has disparado aquí. Elige otra casilla.")
                    continue
                disparos_jugador.add(casilla) 
                break
            except ValueError:
                print("Debes introducir números válidos.")

        acierto = disparar(casilla, tablero_maquina)
        if acierto is True:
            print("¡Tocado!")
        elif acierto is False:
            print("Agua.")
        else:
            print("Ya habías disparado ahí.")

        if not np.any(tablero_maquina == "O"):
            print("¡Has ganado! Todos los barcos enemigos han sido hundidos.")
            break

        print("\nTurno de la máquina:")
        casilla_maquina = random.choice(casillas_disponibles(tablero_jugador))
        disparos_maquina.add(casilla_maquina)
        acierto_maquina = disparar(casilla_maquina, tablero_jugador)

        if acierto_maquina is True:
            print(f"La máquina ha tocado en {casilla_maquina}.")
        else:
            print(f"La máquina falla en {casilla_maquina}.")

        if not np.any(tablero_jugador == "O"):
            print("La máquina ha ganado. Has perdido.")
            break

        print("\nTu tablero actual:")
        mostrar_tablero(tablero_jugador)


if __name__ == "__main__":
    juego_vs_maquina()
