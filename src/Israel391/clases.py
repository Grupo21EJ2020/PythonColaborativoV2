class Libro():
    def __init__(self,autor,numpaginas,editorial):
        self.autor=autor
        self.numpaginas=numpaginas
        self.editorial=editorial
    def imprimirInfo(self):
        print(f'Autor: {self.autor}, numpaginas: {self.numpaginas}, editorial: {self.editorial}')

class Bicicleta():
    def __init__(self,color,modelo,categoria):
        self.color=color
        self.modelo=modelo
        self.categoria=categoria
    def imprimirInfo(self):
        print(f'Color: {self.color}, Modelo: {self.modelo}, Categoria: {self.categoria}')

class Perfume():
    def__init__(self,marca,edicion):
        self.marca=marca
        self.edicion=edicion
    def imprimirInfo(self):
        print(f'Marca: {self.marca}, Edicion: {self.edicion}')