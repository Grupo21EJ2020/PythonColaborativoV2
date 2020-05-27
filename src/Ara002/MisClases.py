class LaptopC():
    def __init__(self,marca,color):
        self.marca = marca
        self.color = color
    
    def imprimirinfo(self):
        print(f"Marca: {self.marca} Color: {self.color}")


class Celular():
    def __init__(self,marca,precio):
        self.marca = marca
        self.precio = precio
    
    def imprimirinfo(self):
        print(f"Marca: {self.marca} Precio: {self.precio}")

class Libreta():
    def __init__(self,tipo,precio):
        self.tipo = tipo
        self.precio = precio
    
    def imprimirinfo(self):
        print(f"tipo: {self.tipo} precio: {self.precio}")