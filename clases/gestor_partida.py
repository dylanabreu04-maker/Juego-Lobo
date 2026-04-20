from jugador_del_juego import jugador_del_juego
from lobo import lobo

class gestorPartida(lobo):  
    def __init__(self):
        self.jugadores =[]

    def anadirJugador(self,nombre, type):  
        self.jugadores.append(jugador_del_juego(nombre,type)) 
        super().__init__(nombre)
        self.type = type
        
    def VotacionDia(self, NombreVotado):
        for j in self.jugadores:
            if j.Nombre == NombreVotado:
                if j.esta_vivo == True:
                    j.esta_vivo=False
                    return "El pueblo ha linchado a " + NombreVotado + " en la hoguera."
        return "Nadie fue linchado."    
        

    def ComprobarVictoria(self):  
        
        list = sum(1 for j in self.jugadores if j.rol == "lobo" and j.esta_vivo)
        dict = sum(1 for j in self.jugadores if j.rol != "lobo" and j.esta_vivo)
        
        if list >= dict:
            return "¡Victoria de los Lobos!"
        elif list ==0:
            return "¡Victoria de los Aldeanos!"
        return "La partida debe continuar..."
