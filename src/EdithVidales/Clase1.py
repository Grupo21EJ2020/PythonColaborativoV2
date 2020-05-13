class FavoritoColor():
    def __init__(self, Nombre, Color):
        self.Nombre = Nombre
        self.Color = Color

    def ImprimirInfo(self):
        print(f"El color favorito de {self.Nombre} es {self.Color}")
