class serie():
    def __init__(self, titulo, genero, horario):
        self.titulo = titulo
        self.genero = genero
        self.horario = horario
    
    def imprimirinfo(self):
        print(f"Titulo: {self.titulo} \n Genero: {self.genero} \n horario: {self.horario}")