class Videojuego():
    def __init__ (self, titulo, plataforma, formato ):
        self.titulo = titulo
        self.plataforma = plataforma
        self.formato = formato
    
    def imprimirInfo(self):
        print(f"El titulo del videojuego es {self.titulo}, esta disponible en {self.plataforma} y esta en formato{self.formato}")