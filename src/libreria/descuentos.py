def validar_descuento(descuento):

    if descuento < 0 or descuento > 40:
        raise ValueError("Descuento inválido")


def aplicar_descuento(precio, descuento):

    validar_descuento(descuento)

    return precio - (precio * descuento / 100)