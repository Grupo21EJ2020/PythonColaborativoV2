class Automovil():
    def __init__(self, color, cilindro, nombre):
        self.color = color
        self.cilindro = cilindro
        self.nombre = nombre
    def imprimirinfo(self):
        print(f"Color: {self.color} Cilindros: {self.cilindro} Nombre: {self.nombre}")

class Zapato():
    def __init__(self, color, precio, marca):
        self.color = color
        self.precio = precio
        self.marca = marca
    def imprimirinfo(self):
        print(f"Color: {self.color} Precio: {self.precio} Marca: {self.marca}")

class Marcador():
    def __init__(self, Marca, Color, Tipo):
        self.Marca = Marca
        self.Color = Color 
        self.Tipo = Tipo

    def imprimirinfo(self):
        print(f"Marca: {self.Marca} Color: {self.Color} Tipo: {self.Tipo}")

        
