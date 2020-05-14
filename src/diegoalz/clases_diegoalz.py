class Automovil():
    def __init__(self, modelo, precio):
        self.modelo = modelo
        self.precio = precio
    
    def imprimirinfo(self):
        print(f"Modelo: {self.modelo} \n Precio: {self.precio} \n")

class Camisa():
    def __init__(self, marca, precio, talla):
        self.modelo = marca
        self.precio = precio
        self.talla = talla
    
    def imprimirinfo(self):
        print(f"Modelo: {self.modelo} \n Precio: {self.precio} \n Talla: {self.talla} \n")

class serie():
    def __init__(self, titulo, genero, fecha):
        self.titulo = titulo
        self.genero = genero
        self.fecha = fecha
    
    def imprimirinfo(self):
        print(f"Titulo: {self.titulo} \n Genero: {self.genero} \n fecha de emisión: {self.fecha} \n")