class XboxOne():
    def __init__(self,version,color):
        self.version = version
        self.color = color
    
    def imprimirinfo(self):
        print(f"Version: {self.version} Color: {self.color}")


class Celular():
    def __init__(self,marca,precio):
        self.marca = marca
        self.precio = precio
    
    def imprimirinfo(self):
        print(f"Marca: {self.marca} Precio: {self.precio}")

class Iphone():
    def __init__(self,version,capacidad):
        self.version = version
        self.capacidad = capacidad
    
    def imprimirinfo(self):
        print(f"Version: {self.version} Capacidad: {self.capacidad}")