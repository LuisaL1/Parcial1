from src.libreria.descuentos import aplicar_descuento

IVA = 0.19


def calcular_precio_final(precio, descuento):

    precio_con_descuento = aplicar_descuento(precio, descuento)

    return precio_con_descuento + (precio_con_descuento * IVA)