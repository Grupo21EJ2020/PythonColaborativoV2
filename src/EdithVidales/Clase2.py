class LugarPreferido():
    def __init__(self, sitio, valoracion):
        self.sitio = sitio
        self.valoracion = valoracion

    def ImprimirInfo(self):
        print(f"Mi lugar favorito es {self.sitio} con una valoración de {self.valoracion}")