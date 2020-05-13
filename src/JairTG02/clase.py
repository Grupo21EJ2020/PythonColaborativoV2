class Tenis ():
    def __init__(self, marca, color, talla):
        self.marca = marca
        self.color = color
        self.talla = talla
    def imprimirInfo (self):
        print(f'Marca: {self.marca}, Color : {self.color}, Talla: {self.talla}')