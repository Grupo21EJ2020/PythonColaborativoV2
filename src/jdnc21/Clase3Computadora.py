class Computadora():
    def __init__(self, marca, nombre, numserie, nummodelo, precio):
        self.marca = marca
        self.nombre = nombre 
        self.numserie = numserie 
        self.nummodelo = nummodelo 
        self.precio = precio
        self.categoria = categoria

    def imprimirinfo(self):
        print(f"Marca: {self.marca} Nombre: {self.nombre} NumSerie: {self.numserie} NumModelo: {self.nummodelo} Precio {self.precio} Categoria: {self.categoria}")
         