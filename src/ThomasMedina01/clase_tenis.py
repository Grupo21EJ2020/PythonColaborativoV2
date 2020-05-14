class Tenis():
    def __init__ (self, marca, color, talla):
        self.marca = marca
        self.color = color
        self.talla = talla
    
    def imprimirInfo(self):
        print(f"Los tenis son de color {self.color} de la marca {self.marca} y del numero {self.talla}")