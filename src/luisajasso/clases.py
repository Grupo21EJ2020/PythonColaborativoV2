class Computadoras():
    def __init__(self, marca,precio,color):
        self.marca = marca
        self.precio = precio
        self.color = color
    def ImprimirInfo(self):
        print(f"La computadora es de la marca {self.marca} del precio {self.precio} del color {self.color}")
    
      

class Materias():
    def __init__(self, nombre, calificacion, grupo):
        self.nombre = nombre
        self.calificacion = calificacion
        self.grupo = grupo
    def ImprimirInfo(self):
        print(f"La materia se llama{self.nombre} con la calificacion {self.calificacion} del grupo{self.grupo}")
    
    

class Lentes():
    def __init__ (self,modelo, precio, graduacion):
        self.modelo = modelo
        self.precio = precio
        self.graduacion = graduacion
    def ImprimirInfo(self):
        print(f"Los lentes son del modelo{self.modelo} con el precio{self.precio} y con una graduacion de {self.graduacion}")
    





