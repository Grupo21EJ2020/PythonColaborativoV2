class Instrumento():
    def __init__(self, marca, nombre, idproducto, precio, categoria):
        self.marca = marca
        self.nombre = nombre 
        self.idproducto = idproducto  
        self.precio = precio
        self.categoria = categoria

    def imprimirinfo(self):
        print(f"Marca: {self.marca} Nombre: {self.nombre} IdProducto: {self.idproducto} Precio: {self.precio} Categoria {self.categoria}")