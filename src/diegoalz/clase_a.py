class Automovil():
    def __init__(self, modelo, precio):
        self.modelo = modelo
        self.precio = precio
    
    def imprimirinfo(self):
        print(f"Modelo: {self.modelo} \n Precio: {self.precio}")