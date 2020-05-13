class Computadora():
    def __init__(self,marca,precio):
        self.marca = marca
        self.precio = precio
    
    def imprimirInfo(self):
        print(f"Marca: {self.marca} Precio: {self.precio}")

class Celular():
    def __init__(self,marca,precio,color):
        self.marca = marca
        self.precio = precio
        self.color = color
    
    def imprimirInfo(self):
        print(f"Marca: {self.marca} Precio: {self.precio} Color: {self.color}")

class Impresora():
    def __init__(self,precio,color,velocidad):
        self.precio = precio
        self.color = color
        self.velocidad = velocidad
    
    def imprimirInfo(self):
        print(f"Precio: {self.precio} Color: {self.color} Velocidad: {self.velocidad}")