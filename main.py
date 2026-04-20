import os  
import sys

from clases import gestorPartida, jugador_del_juego

from logica.metodos import anadirJugador, AccionNocturna




# --- Ejecución caótica ---
def crear_partida():
    juego = gestorPartida()
    jugadores = [
        ("Nacho", "lobo"),
        ("Elena", "vidente"),
        ("Carlos", "aldeano")
    ]
    
    for nombre, rol in jugadores:
        juego.anadirJugador(nombre, rol)
    
    return juego


def ejecutar_partida(juego):
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