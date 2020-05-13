class Libro():
    def __init__(self,autor,numpaginas,editorial):
        self.autor=autor
        self.numpaginas=numpaginas
        self.editorial=editorial
    def imprimirInfo(self):
        print(f'Autor: {self.autor}, numpaginas: {self.numpaginas}, editorial: {self.editorial}')