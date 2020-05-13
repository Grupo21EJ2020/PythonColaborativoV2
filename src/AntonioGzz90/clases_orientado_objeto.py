#PRIMER CLASE
class Saludo():
    def __init__ (self,persona,saludo):
        self.persona = persona
        self.saludo = saludo

    def imprimirSaludo(self):
        print(f"Hola {self.persona}, {self.saludo}")
    