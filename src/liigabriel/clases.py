class Libreta():
    def __init__(self, marca,precio):
        self.marca = marca
        self.precio = precio

    def imprimirinfo(self):
        print(f"Marca: {self.marca} Precio: {self.precio}")


class Mouse():
    def __init__(self, marca,color):
        self.marca = marca
        self.color = color

    def imprimirinfo(self):
        print(f"Marca: {self.marca} Color: {self.color}")


class Ventilador():
    def __init__(self, marca,color,num_velocidades):
        self.marca = marca
        self.color = color
        self.num_velocidades= num_velocidades


    def imprimirinfo(self):
        print(f"Marca: {self.marca} Color: {self.color} No.Vel: {self.num_velocidades}")


