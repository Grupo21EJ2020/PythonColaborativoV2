class Ropa():
    def __init__(self, marca, precio, talla):
        self.marca = marca
        self.precio = precio
        self.talla = talla

    def imprimirInfo(self):
        print( f"Marca: {self.marca}\n Precio: {self.precio}\n Talla: {self.talla}" )
