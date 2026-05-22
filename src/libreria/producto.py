class Producto:

    def __init__(self, nombre, precio_base):

        self.validar_precio(precio_base)

        self.nombre = nombre
        self.precio_base = precio_base

    @staticmethod
    def validar_precio(precio):

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero")