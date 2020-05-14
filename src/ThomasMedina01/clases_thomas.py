class Carro():
    def __init__ (self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def imprimirInfo(self):
        print(f"El carro es un modelo {self.modelo} de la marca {self.marca} del año {self.año}")


class Motocicleta():
    def __init__ (self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def imprimirInfo(self):
        print(f"La Motocicleta es un modelo {self.modelo} de la marca {self.marca} del año {self.año}")


class Pantalon():
    def __init__ (self, marca, color, material):
        self.marca = marca
        self.color = color
        self.material = material
    
    def imprimirInfo(self):
        print(f"El pantalon es de color {self.color} de la marca {self.marca} y esta hecho de {self.material}")

    
class Persona():
    def __init__ (self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def imprimirInfo(self):
        print(f"El nombre de la persona es {self.nombre}, quien es {self.nacionalidad} y tiene {self.edad} años.")