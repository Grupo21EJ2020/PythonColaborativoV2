class Libretas():
    def __init__ ( self, hojas, tipo ):
        self.hojas = hojas
        self.tipo = tipo

    def imprimirinfo(self):
        print(f"Hojas: {self.hojas} tipo: {self.tipo}")

class Zapatos():
    def __init__ (self, talla, color):
        self.talla = talla
        self.color = color 

    def imprimirinfo(self):
        print(f"talla: {self.talla} color: {self.color")

class Libro():
    def __init__ (self, tama�o, materia):
        self.tama�o = tama�o
        self.materia = materia 

    def imprimirinfo(self):
        print(f"tama�o: {self.tama�o} materia {self.materia")
