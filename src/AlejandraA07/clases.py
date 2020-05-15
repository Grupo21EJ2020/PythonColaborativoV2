class Libro():
    def __init__(self, titulo,autor,editorial):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        

    def imprimirinfo(self):
        print(f"Titulo: {self.titulo}\n Autor: {self.autor}\n Editorial: {self.editorial}")


class Alumno():
    def __init__(self, matricula,nombre,carrera):
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera

    def imprimirinfo(self):
        print(f"Matricula: {self.matricula}\n Nombre: {self.nombre}\n Carrera: {self.carrera}")


class Pelicula():
    def __init__(self, titulo, genero, duracion):
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion


    def imprimirinfo(self):
        print(f"Titulo: {self.titulo}\n Genero: {self.genero}\n Duracion: {self.duracion}")
        


