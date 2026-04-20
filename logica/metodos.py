from ..clases import jugador_del_juego, gestor_partida

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


def AccionNocturna(self, objetivo=None):  
    if not self.esta_vivo:
        return f"{self.Nombre} está muerto."
        
    if self.rol=="lobo": 
        if objetivo: 
            objetivo.esta_vivo=False
            return f"El lobo {self.Nombre} ha eliminado a {objetivo.Nombre}."
    elif self.rol== "vidente":
        if objetivo: 
            return f"La vidente {self.Nombre} ve que {objetivo.Nombre} es {objetivo.rol}."
    elif self.rol == "aldeano":
        return f"El aldeano {self.Nombre} duerme profundamente."
    return "Rol desconocido."

def comprobar_victoria(self):
        lobos_vivos = sum(1 for j in self.jugadores if j.rol == "lobo" and j.esta_vivo)
        aldeanos_vivos = sum(1 for j in self.jugadores if j.rol != "lobo" and j.esta_vivo)

        if lobos_vivos >= aldeanos_vivos:
            return "¡Victoria de los Lobos!"
        elif lobos_vivos == 0:
            return "¡Victoria de los Aldeanos!"
        return "La partida debe continuar..."

def ejecutar_partida(juego):
    accion = juego.jugadores[0].AccionNocturna(juego.jugadores[2])
    victoria = juego.ComprobarVictoria()
    
    print(accion)
    print(victoria)

def crear_partida():
    juego = gestorPartida()
    jugadores = [
        ("Nacho", "lobo"),
        ("Elena", "vidente"),
        ("Carlos", "aldeano")
    ]
    
    for nombre, rol in jugadores:
        juego.anadirJugador(nombre, rol)