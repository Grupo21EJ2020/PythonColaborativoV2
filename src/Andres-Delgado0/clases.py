class Humano():
    def __init__(self, raza, nombre, estatura, edad):
        self.raza = raza
        self.nombre = nombre
        self.estatura = estatura
        self.edad = edad
    
    def imprimirinfo(self):
        print(f"Raza: {self.raza} Nombre: {self.nombre} Estatura: {self.estatura}cm Edad: {self.edad}años")



class Articulo():
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    
    def imprimirinfo(self):
        print(f"Nombre: {self.nombre} Cantidad: {self.cantidad} Precio: ${self.precio}")


class Personaje():
    def __init__(self, nombre, aparicion, papeljerarquico):
        self.nombre = nombre
        self.aparicion = aparicion
        self.papeljerarquico = papeljerarquico
    
    def imprimirinfo(self):
        print(f"Nombre: {self.nombre} Aparicion: {self.aparicion} Papeljerarquico: {self.papeljerarquico}")