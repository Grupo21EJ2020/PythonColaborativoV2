class Tenis ():
    def __init__(self, marca, color, talla):
        self.marca = marca
        self.color = color
        self.talla = talla
    def imprimirInfo (self):
        print(f'Marca: {self.marca}, Color : {self.color}, Talla: {self.talla}')

class Jersey ():
    def __init__(self, marca, talla, equipo):
         self.marca = marca
         self.talla = talla
         self.equipo = equipo
    def imprimirInfo (self):
        print(f'Marca: {self.marca}, Talla : {self.talla}, Equipo: {self.equipo}')

class Equipo ():
    def __init__(self, deporte, añoFundacion, campeonatos):
        self.deporte = deporte
        self.añoFundacion = añoFundacion
        self.campeonatos = campeonatos
    def imprimirInfo (self):
        print(f'Deporte:{self.deporte}, Año de Fundacion:{self.añoFundacion}, Campeonatos: {self.campeonatos}')
        

