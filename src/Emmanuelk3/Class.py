class Telefono():
    def __init__(self,Marca,Precio):
        self.Marca = Marca
        self.Precio = Precio
     
        
    def imprimirinfo(self):
        print(f"Marca: {self.Marca} Precio: {self.Precio}")
