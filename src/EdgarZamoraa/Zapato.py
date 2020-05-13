class Zapato():
    def __init__(self, color, precio, marca):
        self.color = color
        self.precio = precio
        self.marca = marca
    def imprimirinfo(self):
        print(f"Color: {self.color} Precio: {self.precio} Marca: {self.marca}")