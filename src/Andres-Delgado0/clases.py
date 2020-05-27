class Humano():
    def __init__(self, raza, nombre, estatura, edad, pais, religion):
        self.raza = raza
        self.nombre = nombre
        self.estatura = estatura
        self.edad = edad
        self.pais
        self.religion
    
    def imprimirinfo(self):
        print(f"Raza: {self.raza} Nombre: {self.nombre} Estatura: {self.estatura}cm Edad: {self.edad}años")
        print(f"Pais: {self.pais} Religion: {self.religion}")

class Materia():
    def __init__(self, nombre, descripcion, areaconocimiento, facultad, maestro):
        self.nombre = nombre
        self.descripcion = descripcion
        self.areaconocimiento = areaconocimiento
        self.facultad = facultad
        self.maestro = maestro

    def imprimirinfo(self):
        print(f"Nombre: {self.nombre} Descripcion: {self.descripcion}") 
        print(f"Area de conocimiento: {self.areaconocimiento} Facultad: {self.facultad}")
        print(f" Maestro: {self.maestro}" ) 
        
class Personaje():
    def __init__(self, nombre, aparicion, papeljerarquico, nacionalidad):
        self.nombre = nombre
        self.aparicion = aparicion
        self.papeljerarquico = papeljerarquico
        self.nacionalidad
        
    def imprimirinfo(self):
        print(f"Nombre: {self.nombre} Aparicion: {self.aparicion} Papeljerarquico: {self.papeljerarquico}")
        print(f"Nacionalidad: {self.nacionalidad}")