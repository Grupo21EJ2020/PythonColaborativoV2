class Cancion():
    def __init__(self, nombre, cancion, duracion):
        self.nombre = nombre
        self.cancion = cancion
        self.duracion = duracion
    
    def imprimirinfo(self):
        print(f"Nombre del artista: {self.nombre} \nNombre de la canción: {self.cancion} \nDuración: {self.duracion} min")

class Carro():
    def __init__(self, marca, nombrecarro, anyo):
        self.marca = marca
        self.nombrecarro = nombrecarro
        self.anyo = anyo

    def imprimircarro(self):
        print(f"Marca del carro: {self.marca} \nNombre: {self.nombrecarro} \nAño del carro: {self.anyo}")

class Pelicula():
    def __init__(self, titulo, fecha, duracion, clasificacion):
        self.titulo = titulo
        self.fecha = fecha
        self.duracion = duracion
        self.clasificacion = clasificacion
    
    def imprimirpeli(self):
        print(f"Título de la película: {self.titulo}\nFecha de lanzamiento: {self.fecha}\nDuración de la película: {self.duracion}\nClasificación de la película: {self.clasificacion}")
