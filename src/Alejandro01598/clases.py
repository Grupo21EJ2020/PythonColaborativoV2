class Auto():
    def _init_(self,modelo,marca):
        self.modelo = modelo   
        self.marca = marca

    def imprimirinfo(self):
        print(f"Modelo: {self.modelo} Marca: {self.marca}")  
          
class Alumno():
    def _init_(self,carrera,semestre):
        self.carrera=carrera
        self.semestre=semestre
        
    def imprimirinfo(self):
        print(f"Carrera : {self.carrera} Semestre:{self.semestre}")
