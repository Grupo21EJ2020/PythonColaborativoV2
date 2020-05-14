class Telefono():
    def __init__(self,Marca,Precio):
        self.Marca = Marca
        self.Precio = Precio
     
        
    def imprimirinfo(self):
        print(f"Marca: {self.Marca} Precio: {self.Precio}")



class Bicicletas():
    def __init__(self,Color,Modelo):
        self.Color = Color
        self.Modelo = Modelo 

    def imprimirinfo(self):
        print(f"Color: {self.Color} Modelo: {self.Modelo}")



class Tenis():
    def __init__(self,Tipo,Talla):
        self.Tipo = Tipo
        self.Talla = Talla
    
    def imprimirinfo(self):
        print(f"Tipo: {self.Tipo} Talla: {self.Talla}")


class Mouse():
    def __init__(self,Tamaño,Numerodevelocidades):
        self.Tamaño = Tamaño
        self.Numerodevelocidades = Numerodevelocidades

  def imprimirinfo(self):
      print(f"Tamaño: {self.Tamaño} Numerodevelocidades: {self.Numerodevelocidades})
      