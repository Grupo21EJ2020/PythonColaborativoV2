class Libretas():
    def __init__ ( self, hojas, tipo ):
        self.hojas = hojas
        self.tipo = tipo

    def imprimirinfo(self):
        print(f"Hojas: {self.hojas} tipo: {self.tipo}")