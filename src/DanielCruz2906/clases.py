class Automovil():
    def __init__(self, marca, precio, año):
        self.marca = marca
        self.precio = precio
        self.año = año
    
    def imprimirinfo(self):
        print(f"Marca: {self.marca}\nAño: {self.año}\n")

class Computadora():
    def __init__(self, procesador, gpu, ram):
        self.procesador = procesador
        self.gpu = gpu
        self.ram = ram
    
    def imprimirinfo(self):
        print(f"Procesador: {self.procesador}\nTarjeta Grafica: {self.gpu}\n")

class Television():
    def __init__(self, tamaño, precio, marca):
        self.tamaño = tamaño
        self.precio = precio
        self.marca = marca
    
    def imprimirinfo(self):
        print(f"Tamaño: {self.tamaño}\nPrecio: {self.precio}\nMarca: {self.marca}\n")


