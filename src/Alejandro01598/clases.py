class Auto():
    def _init_(self,modelo,marca):
        self.modelo = modelo   
        self.marca = marca

    def imprimirinfo(self):
          print(f"Modelo: {self.modelo} Marca: {self.marca}")  