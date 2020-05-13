class Camisa():
    def __init__(self, marca, precio, talla):
        self.modelo = marca
        self.precio = precio
        self.talla = talla
    
    def imprimirinfo(self):
        print(f"Modelo: {self.modelo} \n Precio: {self.precio} \n Talla: {self.talla}")