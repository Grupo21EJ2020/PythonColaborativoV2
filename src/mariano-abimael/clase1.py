class Rollodepapel():
    def __init__(self, marca, precio, canthojas):
        self.marca = marca
        self.precio = precio
        self.canthojas = canthojas
    
    def Imprimirinfo(self):
        print(f"Marca {self.marca} Precio: {self. precio} Canthojas: {self.canthojas}")