import os  
import sys

from clases import gestorPartida, jugador_del_juego

from logica.metodos import anadirJugador, AccionNocturna




def crear_partida():
    """
    Crea y realiza la partida inicail con un numero determinado de jugadores ya establecidos.

    Returns:
        gestorPartida: Objeto de la partida con los jugadores ya añadidos.
    """
    juego = gestorPartida()
    jugadores = [
        ("Nacho", "lobo"),
        ("Elena", "vidente"),
        ("Carlos", "aldeano")
    ]
    
    for nombre, rol in jugadores:
        juego.anadirJugador(nombre, rol)
    
    return


def ejecutar_partida(juego):
    """
    Ejecuta la partida realiza una acción nocturna y comprueba
    si alguna condición de victoria se ha cumplido.

    Args:
        juego (gestorPartida): lo que contiene los jugadores
            y su estado actual.

    Returns:
        None: Imprime el resultado de la acción y la condición
        de victoria.
    """
    accion = juego.jugadores[0].AccionNocturna(juego.jugadores[2])
    victoria = juego.ComprobarVictoria()
    
    print(accion)
    print(victoria)


if __name__ == "__main__":
    juego = crear_partida()
    ejecutar_partida(juego)

# Intenta estructurar el main.py con el siguiente orden.
# --- FASE 1: LA NOCHE 🌙 ---
# Comprobamos estado antes de que amanezca
# --- FASE 2: EL DÍA ☀️ ---
# El motor de la partida ejecuta el linchamiento
# --- FINAL DE LA PARTIDA ---