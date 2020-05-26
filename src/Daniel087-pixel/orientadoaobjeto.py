class Revista():
    def __init__(self,autor,numpaginas,editorial):
        self.autor=autor
        self.numpaginas=numpaginas
        self.editorial=editorial
    def infoview(self):
        print(f'Autor: {self.autor}, numpaginas: {self.numpaginas}, editorial: {self.editorial}')

class Motocicleta():
    def __init__(self,color,modelo,tipo):
        self.color=color
        self.modelo=modelo
        self.tipo=tipo
    def infoview(self):
        print(f'Color: {self.color}, Modelo: {self.modelo}, Tipo: {self.tipo}')

class Edificio():
    def __init__(self,tamaño,giro):
        self.tamaño=tamaño
        self.giro=giro
    def infoview(self):
        print(f'Tamaño: {self.tamaño}, Giro: {self.giro}')