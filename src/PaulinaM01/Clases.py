class Bocina():
    def __init__(self,marca,tipo,precio):
        self.marca=marca
        self.tipo=tipo
        self.precio=precio

    def imprimirinfo(self):
        print(f"Marca:{self.marca} Tipo:{self.tipo} Precio:{self.precio}")
    
class Consola_Videojuegos():
    def __init__(self,marca,precio):
        self.marca=marca
        self.precio=precio

    def imprimirinfo(self):
        print(f"Marca:{self.marca} Precio:{self.precio}")

class Audifonos():
    def __init__(self,marca,color,precio):
        self.marca=marca
        self.color=color
        self.precio=precio

    def imprimirinfo(self):
        print(f"Marca:{self.marca} Color:{self.color} Precio:{self.precio}")
        
    