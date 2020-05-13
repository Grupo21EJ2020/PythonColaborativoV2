class Cancion():
    def __init__(self, nombre, cancion, duracion):
        self.nombre = nombre
        self.cancion = cancion
        self.duracion = duracion
    
    def imprimirinfo(self):
        print(f"Nombre del artista: {self.nombre} \nNombre de la canción: {self.cancion} \nDuración: {self.duracion} min")