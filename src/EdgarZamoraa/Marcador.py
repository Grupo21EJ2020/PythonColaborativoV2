class Marcador():
    def __init__(self, Marca, Color, Tipo):
        self.Marca = Marca
        self.Color = Color 
        self.Tipo = Tipo

    def imprimirinfo(self):
        print(f"Marca: {self.Marca} Color: {self.Color} Tipo: {self.Tipo}")