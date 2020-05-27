class Humano():
    def __init__(self, raza, nombre, estatura, edad):
        self.raza = raza
        self.nombre = nombre
        self.estatura = estatura
        self.edad = edad
    
    def imprimirinfo(self):
        print(f"Raza: {self.raza} Nombre: {self.nombre} Estatura: {self.estatura}cm Edad: {self.edad}años")

class Materia():
    def __init__(self, nombre, descripcion, areaconocimiento, facultad, maestro):
        self.nombre = nombre
        self.descripcion = descripcion
        self.areaconocimiento = areaconocimiento
        self.facultad = facultad
        self.maestro = maestro
    def imprimirinfo(self):
        print(f"Nombre: {self.nombre} Descripcion: {self.descripcion}") 
        print(f"Area de conocimiento: {self.areaconocimiento} Facultad {self.facultad}")
        print(f" Maestro: {self.maestro}" ) 
        
class Personaje():
    def __init__(self, nombre, aparicion, papeljerarquico):
        self.nombre = nombre
        self.aparicion = aparicion
        self.papeljerarquico = papeljerarquico
    
    def imprimirinfo(self):
        print(f"Nombre: {self.nombre} Aparicion: {self.aparicion} Papeljerarquico: {self.papeljerarquico}")