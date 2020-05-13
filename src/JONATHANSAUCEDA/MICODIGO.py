class Banco ():
    def __init__(self,LigasDeFut,Equipo,Titulos):
        self.LigasDeFut = LigasDeFut
        self.Equipo = Equipo
        self.Titulos = Titulos

    def imprimirinfo(self):
        print(f"LigasDeFut: {self.LigasDeFut} \n Equipo:{self.Equipo} \n Titulos:{self.Titulos}")


