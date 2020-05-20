class Refrigerador():
    def __innit__(self, marca, precio, tamaño):
        self.marca = marca
        self.precio = precio
        self.tamaño = tamaño
    def Imprimirinfo(self):
        print(f"Marca: {self.marca} Precio: {self.precio} Tamaño: {self.tamaño}")