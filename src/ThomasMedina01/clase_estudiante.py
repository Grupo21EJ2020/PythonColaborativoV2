class Estudiante():
    def __init__ (self, nombre, matricula, promedio):
        self.nombre = nombre
        self.matricula = matricula
        self.promedio = promedio
    
    def imprimirInfo(self):
        print(f"El estudiante se llama {self.nombre}, su matricula es {self.matricula} y tiene un promedio general de {self.promedio}.")