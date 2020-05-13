class Taladro():
    def __init__(self,velocidades,tipo):
        self.velocidades = velocidades
        self.tipo = tipo

    def imprimirinfo(self):
        print(f"Taladro: {self.velocidades} Tipo: {self.tipo}")

class Desarmador():
    def __init__(self,estrella,plano):
        self.estrella = estrella
        self.plano = plano

    def imprimirinfo(self):
        print(f"Desarmador tipo: {self.estrella} : {self.plano}")