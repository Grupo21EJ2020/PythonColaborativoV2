class Ropa():
    def __init__(self, marca, precio, talla):
        self.marca = marca
        self.precio = precio
        self.talla = talla

    def imprimirInfo(self):
        print( f"Marca: {self.marca}\n Precio: {self.precio}\n Talla: {self.talla}" )

#CLASE NUMERO 2---
class Videojuegos():
    def __init__(self, genero, tamaño, duracion):
        self.genero = genero
        self.tamaño = tamaño
        self.duracion = duracion

    def imprimirInfo(self):
        print( f"Genero: {self.genero}\n Tamaño: {self.tamaño}\n Duracion: {self.duracion}" )

#CLASE NUMERO 3---
class Muebles ():
    def __init__(self, nombre, material, garantia):
        self.nombre = nombre
        self.material = material
        self.garantia = garantia

    def imprimirInfo(self):
        print(f"Nombre: {self.nombre}\n Material {self.material}\n Garantia{self.garantia}")