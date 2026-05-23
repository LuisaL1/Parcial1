from src.libreria.descuentos import aplicar_descuento


def calcular_precio_final(precio, descuento):

    precio_con_descuento = aplicar_descuento(precio, descuento)

    precio_final = precio_con_descuento * 1.19

    return precio_final