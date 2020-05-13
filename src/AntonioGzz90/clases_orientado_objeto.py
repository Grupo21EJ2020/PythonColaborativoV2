#PRIMER CLASE

class Saludo():
    def __init__ (self,persona,saludo):
        self.persona = persona
        self.saludo = saludo

    def imprimirSaludo(self):
        print(f"Hola {self.persona}, {self.saludo}")
    
#SEGUNDA CLASE
class Preferencia():
    def __init__(self,primera,segunda,tercera):
        self.primera = primera
        self.segunda = segunda
        self.tercera = tercera

    def imprimirPreferencias(self):
        print(f"Tu primer gusto que nos compartiste fue: {self.primera} \n Segundo apunte que diste a conocer: {self.segunda} \n Y por ultimo y no menos importante: {self.tercera}")

#TERCERA CLASE
class MiembrosdeFamilia():
    def __init__(self,madre,padre,hermano,hermana):
        self.madre = madre
        self.padre = padre
        self.hermano = hermano
        self.hermana = hermana

    def imprimirFamily(self):
        print(f"Tu madre es: {self.madre}")
        print(f"Tu padre es: {self.padre}")
        print(f"Tu hermano es: {self.hermano}")
        print(f"Tu hermana es: {self. hermana}")

