from jugador_del_juego import jugador_del_juego
from lobo import lobo

class gestorPartida(lobo):  
    """
    gestiona l partida incluyendo jugadores, votaciones y el resultado de la partida.

    Esta clase mantiene una lista de jugadores y permite añadir nuevos,
    realizar votaciones durante el día y comprobar hay algun ganador.

    Attributes:
        jugadores (list): Lista de jugadores activos e inactivos en la partida.
    """
    def __init__(self):
        self.jugadores = []

    def anadirJugador(self,nombre, type):
        """
        Añade un nuevo jugador a la partida.

        Args:
            nombre (str): Nombre del jugador.
            type (str): tipo del jugador.
        """  
        self.jugadores.append(jugador_del_juego(nombre,type)) 
        super().__init__(nombre)
        self.type = type
        
    def votacionDia(self, nombre_votado: str):
        """
        Ejecuta la votación del día, eliminando  a un jugador si existe
        y está vivo.

        Args:
            nombre_votado (str): Nombre del jugador.

        Returns:
            str: Resultado de la votación indicando si hubo linchamiento o no.
        """
        for jugador in self.jugadores:
            if jugador.Nombre == nombre_votado and jugador.esta_vivo:
                jugador.esta_vivo = False
                return f"El pueblo ha linchado a {nombre_votado} en la hoguera."
        return "Nadie fue linchado."   
        

    def comprobar_victoria(self):
        """
        comprueba la victoria viendo la cantidad de lobos o aldenaos vivos que hay en la partida

        Args:
            lobos_vivos (int): numero de lobos que hay vivos
            aldeanos_vivos (int): numero de aldeanos vivos que hay
        returns: 
            str: resultado de la vistoria o derrota.
        """
        lobos_vivos = sum(1 for j in self.jugadores if j.rol == "lobo" and j.esta_vivo)
        aldeanos_vivos = sum(1 for j in self.jugadores if j.rol != "lobo" and j.esta_vivo)

        if lobos_vivos >= aldeanos_vivos:
            return "¡Victoria de los Lobos!"
        elif lobos_vivos == 0:
            return "¡Victoria de los Aldeanos!"
        return "La partida debe continuar..."