class Carro():
    def __init__ (self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def imprimirInfo(self):
        print(f"El carro es un modelo {modelo} de la marca {marca} del año {año}")


class Motocicleta():
    def __init__ (self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def imprimirInfo(self):
        print(f"La Motocicleta es un modelo {modelo} de la marca {marca} del año {año}")


class Pantalon():
    def __init__ (self, marca, color, material):
        self.marca = marca
        self.color = color
        self.material = material
    
    def imprimirInfo(self):
        print(f"El pantalon es de color {color} de la marca {marca} y esta hecho de {material}")