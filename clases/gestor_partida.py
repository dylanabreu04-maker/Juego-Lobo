from jugador_del_juego import jugador_del_juego
from lobo import lobo

class gestorPartida(lobo):  
    def __init__(self):
        self.jugadores = []

    def anadirJugador(self,nombre, type):  
        self.jugadores.append(jugador_del_juego(nombre,type)) 
        super().__init__(nombre)
        self.type = type
        
    def votacionDia(self, nombre_votado: str):
        for jugador in self.jugadores:
            if jugador.Nombre == nombre_votado and jugador.esta_vivo:
                jugador.esta_vivo = False
                return f"El pueblo ha linchado a {nombre_votado} en la hoguera."
        return "Nadie fue linchado."   
        

    def comprobar_victoria(self):
        lobos_vivos = sum(1 for j in self.jugadores if j.rol == "lobo" and j.esta_vivo)
        aldeanos_vivos = sum(1 for j in self.jugadores if j.rol != "lobo" and j.esta_vivo)

        if lobos_vivos >= aldeanos_vivos:
            return "¡Victoria de los Lobos!"
        elif lobos_vivos == 0:
            return "¡Victoria de los Aldeanos!"
        return "La partida debe continuar..."