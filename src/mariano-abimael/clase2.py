class Calculadora():
    def __innit__(self, marca, precio, tipo, tamaño):
        self.marca = marca
        self.precio = precio
        self.tipo = tipo 
        self.tamaño = tamaño
    def Imprimirinfo(self):
        print(f"Marca: {self.marca} Precio: {self.precio} Tipo: {self.tipo} Tamaño: {self.tamaño}")